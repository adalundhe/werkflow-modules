import asyncio
import datetime
import re

from werkflow.modules.base import Module
from werkflow_encryption import Encryption
from werkflow_http import HTTP
from werkflow_http.connections.http.models.http import HTTPResponse

from .models.requests.errors import (
    BadRequestError,
    MethodNotAllowedError,
    ResourceNotFoundError,
    ServerFailedError,
    UnauthorizedRequestError,
    UnprocessableContentError,
)
from .models.requests.jira import (
    Issue,
    JiraIssue,
    JiraIssueAssignee,
    JiraIssueBatch,
    JiraIssueDescription,
    JiraIssueFields,
    JiraIssueLink,
    JiraIssueLinkComment,
    JiraIssueLinkKey,
    JiraIssueLinkRefType,
    JiraIssueParent,
    JiraIssuePriority,
    JiraIssueProject,
    JiraIssueReporter,
    JiraIssueType,
)
from .models.requests.jira.content import JiraInlineBlock, JiraTopLevelBlock
from .models.responses.jira import (
    JiraIssueLinkType,
    JiraIssueLinkTypes,
    JiraIssueResponse,
    JiraProject,
    JiraUser,
)
from .models.responses.jira import JiraIssuePriority as JiraIssuePriorityResponse
from .models.responses.jira import JiraIssueType as JiraIssueTypeResponse


class Jira(Module):
    module_enabled = True
    dependencies = ["werkflow-http", "werkflow-encryption"]

    def __init__(self) -> None:
        super().__init__()

        self._loop: asyncio.AbstractEventLoop = None

        self.client = HTTP()
        self.user: str = None

        self._errors_map = {
            (401, 403): UnauthorizedRequestError,
            (400, 400): BadRequestError,
            (404, 404): ResourceNotFoundError,
            (405, 405): MethodNotAllowedError,
            (422, 422): UnprocessableContentError,
            (500, 599): ServerFailedError,
        }

        self._slug_pattern = re.compile(r"[^0-9a-zA-Z]+")
        self._duplicate_dash_pattern = re.compile(r"[-]+")
        self.project_slug: str = None
        self.encryption = Encryption()

    def check_response(self, response: HTTPResponse) -> HTTPResponse:
        if response.status < 200 or response.status >= 400:
            for error_code_range, error in self._errors_map.items():
                min_error_code, max_error_code = error_code_range

                if (
                    response.status >= min_error_code
                    and response.status <= max_error_code
                ):
                    raise error(response.url, response.method, response.status)

        return response

    def slugify(self, project_name: str) -> str:
        project_slug = (
            self._slug_pattern.sub(
                "-",
                project_name,
            )
            .lower()
            .strip("-")
        )

        return self._duplicate_dash_pattern.sub(
            "-",
            project_slug,
        )

    async def create_issue(
        self,
        jira_email: str,
        jira_api_token: str,
        jira_issue_summary: str,
        jira_issue_description: list[JiraTopLevelBlock],
        jira_issue_type: str,
        jira_issue_priority: str,
        jira_issue_reporter: str,
        jira_issue_project: str,
        jira_issue_assignee: str | None = None,
        jira_issue_labels: list[str] | None = None,
        jira_issue_due_date: datetime.datetime | None = None,
        jira_parent_issue: str | None = None,
        organization: str = "datavant",
    ):
        issue_priority = await self.get_matching_priority(
            jira_issue_priority,
            jira_email,
            jira_api_token,
            organization=organization,
        )

        issue_reporter = await self.get_matching_user_by_email(
            jira_issue_reporter, jira_email, jira_api_token, organization=organization
        )

        issue_project = await self.get_jira_project(
            jira_issue_project,
            jira_email,
            jira_api_token,
            organization=organization,
        )

        issue_type = await self.get_matching_project_issue_type(
            jira_issue_type,
            issue_project.id,
            jira_email,
            jira_api_token,
            organization=organization,
        )

        issue_assignee: JiraIssueAssignee | None = None
        if jira_issue_assignee:
            issue_assignee_user = await self.get_matching_user_by_email(
                jira_issue_assignee,
                jira_email,
                jira_api_token,
                organization=organization,
            )
            issue_assignee = JiraIssueAssignee(id=issue_assignee_user.accountId)

        data = JiraIssue(
            fields=JiraIssueFields(
                assignee=issue_assignee,
                description=JiraIssueDescription(content=jira_issue_description),
                issuetype=JiraIssueType(id=issue_type.id),
                duedate=jira_issue_due_date,
                labels=jira_issue_labels,
                parent=JiraIssueParent(key=jira_parent_issue)
                if jira_parent_issue
                else None,
                priority=JiraIssuePriority(id=issue_priority.id),
                reporter=JiraIssueReporter(id=issue_reporter.accountId),
                project=JiraIssueProject(id=issue_project.id),
                summary=jira_issue_summary,
            )
        )

        response = await self.client.post(
            f"https://{organization}.atlassian.net/rest/api/3/issue",
            headers={
                "Content-Type": "application/json",
            },
            auth=(
                jira_email,
                jira_api_token,
            ),
            data=data.model_dump(
                exclude_none=True,
            ),
        )

        checked_response = self.check_response(response)

        return JiraIssueResponse(**checked_response.json())

    async def get_issue(
        self,
        issue_id: str,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):
        response = await self.client.get(
            f"https://{organization}.atlassian.net/rest/api/3/issue/{issue_id}",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        return self.check_response(response)

    async def create_issue_batch(
        self,
        jira_issues: list[Issue],
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):
        created_jira_issues = await asyncio.gather(
            *[
                self._convert_jira_issue_dict_to_request(
                    issue_dict, jira_email, jira_api_token, organization=organization
                )
                for issue_dict in jira_issues
            ]
        )

        data = JiraIssueBatch(issueUpdates=created_jira_issues)

        response = await self.client.post(
            f"https://{organization}.atlassian.net/rest/api/3/issue/bulk",
            auth=(
                jira_email,
                jira_api_token,
            ),
            headers={
                "Content-Type": "application/json",
            },
            data=data.model_dump(exclude_none=True),
        )

        checked_response = self.check_response(response)

        return [JiraIssueResponse(**issue) for issue in checked_response.json()]

    async def _convert_jira_issue_dict_to_request(
        self,
        jira_issue: Issue,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):

        issue_priority = await self.get_matching_priority(
            jira_issue.priority,
            jira_email,
            jira_api_token,
            organization=organization,
        )

        issue_reporter = await self.get_matching_user_by_email(
            jira_issue.reporter,
            jira_email,
            jira_api_token,
            organization=organization,
        )

        issue_project = await self.get_jira_project(
            jira_issue.project,
            jira_email,
            jira_api_token,
            organization=organization,
        )

        issue_type = await self.get_matching_project_issue_type(
            jira_issue.issue_type,
            issue_project.id,
            jira_email,
            jira_api_token,
            organization=organization,
        )

        issue_assignee: JiraIssueAssignee | None = None
        if jira_issue.assignee:
            issue_assignee_user = await self.get_matching_user_by_email(
                jira_issue.assignee,
                jira_email,
                jira_api_token,
                organization=organization,
            )
            issue_assignee = JiraIssueAssignee(id=issue_assignee_user.accountId)

        issue = JiraIssue(
            fields=JiraIssueFields(
                assignee=issue_assignee,
                description=JiraIssueDescription(content=jira_issue.description),
                duedate=jira_issue.due_date,
                labels=jira_issue.labels,
                parent=JiraIssueParent(key=jira_issue.parent_issue)
                if jira_issue.parent_issue
                else None,
                issuetype=JiraIssueType(id=issue_type.id),
                priority=JiraIssuePriority(id=issue_priority.id),
                reporter=JiraIssueReporter(id=issue_reporter.accountId),
                project=JiraIssueProject(id=issue_project.id),
                summary=jira_issue.summary,
            )
        )

        return issue

    async def get_matching_user_by_email(
        self,
        jira_user_email: str,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):
        response = await self.client.get(
            f"https://{organization}.atlassian.net/rest/api/3/user/search?query={jira_user_email}",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        checked_response = self.check_response(response)

        jira_users = [JiraUser(**user) for user in checked_response.json()]

        matching_users = [
            user for user in jira_users if user.emailAddress == jira_user_email
        ]

        assert (
            len(matching_users) > 0
        ), f"No match user found for issue reporter email - {jira_user_email}"

        return matching_users[0]

    async def list_priorities(
        self,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):
        response = await self.client.get(
            f"https://{organization}.atlassian.net/rest/api/3/priority",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        checked_response = self.check_response(response)

        return [
            JiraIssuePriorityResponse(**priority)
            for priority in checked_response.json()
        ]

    async def get_matching_priority(
        self,
        jira_priority: str,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):
        priorities = await self.list_priorities(
            jira_email,
            jira_api_token,
            organization=organization,
        )

        matching_priorities = [
            priority
            for priority in priorities
            if priority.name.lower() == jira_priority.lower()
        ]

        assert (
            len(matching_priorities) > 0
        ), f"No matching priority found for priority - {jira_priority}"

        matching_priority = matching_priorities[0]

        return matching_priority

    async def get_jira_project(
        self,
        jira_project_name_or_id: str,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):
        response = await self.client.get(
            f"https://{organization}.atlassian.net/rest/api/3/project/{jira_project_name_or_id}",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        checked_response = self.check_response(response)

        return JiraProject(**checked_response.json())

    async def get_project_issue_types(
        self,
        project_id: str,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):
        response = await self.client.get(
            f"https://{organization}.atlassian.net/rest/api/3/issuetype/project?projectId={project_id}",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        checked_response = self.check_response(response)

        return [
            JiraIssueTypeResponse(**issue_type)
            for issue_type in checked_response.json()
        ]

    async def get_matching_project_issue_type(
        self,
        issue_type_name: str,
        project_id: str,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):
        jira_issue_types = await self.get_project_issue_types(
            project_id,
            jira_email,
            jira_api_token,
            organization=organization,
        )

        matching_issue_types = [
            issue_type
            for issue_type in jira_issue_types
            if issue_type.name.lower() == issue_type_name.lower()
        ]

        assert (
            len(matching_issue_types) > 0
        ), f"No matching issue type found for - {issue_type_name}"

        return matching_issue_types[0]

    async def get_issue_link_types(
        self,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):
        # issueLinkType
        response = await self.client.get(
            f"https://{organization}.atlassian.net/rest/api/3/issueLinkType",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        checked_response = self.check_response(response)

        return JiraIssueLinkTypes(**checked_response.json())

    async def get_matching_issue_link_type(
        self,
        jira_issue_link_type: str,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ) -> JiraIssueLinkType:
        link_types = await self.get_issue_link_types(
            jira_email, jira_api_token, organization=organization
        )

        issue_link_types: list[JiraIssueLinkType] = link_types.issueLinkTypes

        matching_link_types = [
            link_type
            for link_type in issue_link_types
            if link_type.inward.lower() == jira_issue_link_type.lower()
            or link_type.outward.lower() == jira_issue_link_type
        ]

        assert (
            len(matching_link_types) > 0
        ), f"No matching link type - {jira_issue_link_type} - found."

        return matching_link_types[0]

    async def create_issue_link(
        self,
        jira_issue_link_comment: str,
        jira_from_issue: str,
        jira_to_issue: str,
        jira_issue_link_type: str,
        jira_email: str,
        jira_api_token: str,
        organization: str = "datavant",
    ):
        jira_link_type = await self.get_matching_issue_link_type(
            jira_issue_link_type,
            jira_email,
            jira_api_token,
            organization=organization,
        )

        data = JiraIssueLink(
            comment=JiraIssueLinkComment(
                body=JiraIssueDescription(
                    content=[
                        JiraTopLevelBlock(
                            content=[JiraInlineBlock(text=jira_issue_link_comment)]
                        )
                    ]
                ),
            ),
            inwardIssue=JiraIssueLinkKey(key=jira_from_issue),
            outwardIssue=JiraIssueLinkKey(key=jira_to_issue),
            type=JiraIssueLinkRefType(name=jira_link_type.name),
        )

        return await self.client.post(
            f"https://{organization}.atlassian.net/rest/api/3/issueLink",
            auth=(
                jira_email,
                jira_api_token,
            ),
            headers={"Content-Type": "application/json"},
            data=data.model_dump(exclude_none=True),
        )
