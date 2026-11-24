import asyncio
import datetime
import re
from typing import Any, Dict, List, Tuple, Type

from werkflow_core import Module
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
    dependencies = ["werkflow-http", "pydantic"]

    def __init__(self) -> None:
        super().__init__()

        self.client = HTTP()

        self._errors_map: Dict[Tuple[int, int], Type[Exception]] = {
            (401, 403): UnauthorizedRequestError,
            (400, 400): BadRequestError,
            (404, 404): ResourceNotFoundError,
            (405, 405): MethodNotAllowedError,
            (422, 422): UnprocessableContentError,
            (500, 599): ServerFailedError,
        }

        self._slug_pattern = re.compile(r"[^0-9a-zA-Z]+")
        self._duplicate_dash_pattern = re.compile(r"[-]+")

    def check_response(self, response: HTTPResponse) -> HTTPResponse:
        status = response.status
        url_str = str(response.url)
        method_str = str(response.method or "")

        if status is None:
            raise ServerFailedError(url_str, method_str, 0)

        if status < 200 or status >= 400:
            for (min_error_code, max_error_code), error in self._errors_map.items():
                if min_error_code <= status <= max_error_code:
                    raise error(url_str, method_str, status)

            if status >= 500:
                raise ServerFailedError(url_str, method_str, status)

            raise BadRequestError(url_str, method_str, status)

        return response

    def _parse_json(self, response: HTTPResponse) -> Any:
        payload = response.json()
        if isinstance(payload, Exception):
            raise payload
        return payload

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
        jira_organization: str,
        jira_issue_description: list[JiraTopLevelBlock],
        jira_issue_type: str,
        jira_issue_priority: str,
        jira_issue_project: str,
        jira_issue_assignee: str | None = None,
        jira_issue_due_date: datetime.datetime | datetime.date | str | None = None,
        jira_issue_labels: list[str] | None = None,
        jira_issue_reporter: str | None = None,
        jira_parent_issue: str | None = None,
    ) -> JiraIssueResponse:
        issue_priority = await self.get_matching_priority(
            jira_issue_priority,
            jira_email,
            jira_api_token,
            jira_organization=jira_organization,
        )

        issue_project = await self.get_jira_project(
            jira_issue_project,
            jira_email,
            jira_api_token,
            jira_organization=jira_organization,
        )

        issue_type = await self.get_matching_project_issue_type(
            jira_issue_type,
            issue_project.id,
            jira_email,
            jira_api_token,
            jira_organization=jira_organization,
        )

        issue_reporter: JiraIssueReporter | None = None
        if jira_issue_reporter:
            matching_user = await self.get_matching_user_by_email(
                jira_issue_reporter,
                jira_email,
                jira_api_token,
                jira_organization=jira_organization,
            )

            issue_reporter = JiraIssueReporter(id=matching_user.accountId)

        issue_assignee: JiraIssueAssignee | None = None
        if jira_issue_assignee:
            issue_assignee_user = await self.get_matching_user_by_email(
                jira_issue_assignee,
                jira_email,
                jira_api_token,
                jira_organization=jira_organization,
            )
            issue_assignee = JiraIssueAssignee(id=issue_assignee_user.accountId)

        data = JiraIssue(
            fields=JiraIssueFields(
                assignee=issue_assignee,
                description=JiraIssueDescription(content=list(jira_issue_description)),
                issuetype=JiraIssueType(id=issue_type.id),
                duedate=jira_issue_due_date,
                labels=jira_issue_labels,
                parent=JiraIssueParent(key=jira_parent_issue)
                if jira_parent_issue
                else None,
                priority=JiraIssuePriority(id=issue_priority.id),
                reporter=issue_reporter,
                project=JiraIssueProject(id=issue_project.id),
                summary=jira_issue_summary,
            )
        )

        response = await self.client.post(
            f"https://{jira_organization}.atlassian.net/rest/api/3/issue",
            headers={
                "Content-Type": "application/json",
            },
            auth=(
                jira_email,
                jira_api_token,
            ),
            data=data.model_dump(
                mode="json",
                exclude_none=True,
            ),
        )

        checked_response = self.check_response(response)
        return JiraIssueResponse(**self._parse_json(checked_response))

    async def get_issue(
        self,
        issue_id: str,
        jira_email: str,
        jira_api_token: str,
        jira_organization: str,
    ) -> HTTPResponse:
        response = await self.client.get(
            f"https://{jira_organization}.atlassian.net/rest/api/3/issue/{issue_id}",
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
        jira_organization: str,
    ) -> List[JiraIssueResponse]:
        created_jira_issues = list(
            await asyncio.gather(
                *[
                    self._convert_jira_issue_dict_to_request(
                        issue_dict,
                        jira_email,
                        jira_api_token,
                        jira_organization=jira_organization,
                    )
                    for issue_dict in jira_issues
                ]
            )
        )

        data = JiraIssueBatch(issueUpdates=created_jira_issues)

        response = await self.client.post(
            f"https://{jira_organization}.atlassian.net/rest/api/3/issue/bulk",
            auth=(
                jira_email,
                jira_api_token,
            ),
            headers={
                "Content-Type": "application/json",
            },
            data=data.model_dump(mode="json", exclude_none=True),
        )

        checked_response = self.check_response(response)
        payload = self._parse_json(checked_response)
        issues = payload.get("issues", []) if isinstance(payload, dict) else payload

        return [JiraIssueResponse(**issue) for issue in issues]

    async def _convert_jira_issue_dict_to_request(
        self,
        jira_issue: Issue,
        jira_email: str,
        jira_api_token: str,
        jira_organization: str,
    ) -> JiraIssue:
        issue_priority = await self.get_matching_priority(
            jira_issue.priority,
            jira_email,
            jira_api_token,
            jira_organization=jira_organization,
        )

        issue_project = await self.get_jira_project(
            jira_issue.project,
            jira_email,
            jira_api_token,
            jira_organization=jira_organization,
        )

        issue_type = await self.get_matching_project_issue_type(
            jira_issue.issue_type,
            issue_project.id,
            jira_email,
            jira_api_token,
            jira_organization=jira_organization,
        )

        issue_reporter: JiraIssueReporter | None = None
        if jira_issue.reporter:
            matching_user = await self.get_matching_user_by_email(
                jira_issue.reporter,
                jira_email,
                jira_api_token,
                jira_organization=jira_organization,
            )

            issue_reporter = JiraIssueReporter(id=matching_user.accountId)

        issue_assignee: JiraIssueAssignee | None = None
        if jira_issue.assignee:
            issue_assignee_user = await self.get_matching_user_by_email(
                jira_issue.assignee,
                jira_email,
                jira_api_token,
                jira_organization=jira_organization,
            )
            issue_assignee = JiraIssueAssignee(id=issue_assignee_user.accountId)

        return JiraIssue(
            fields=JiraIssueFields(
                assignee=issue_assignee,
                description=JiraIssueDescription(content=list(jira_issue.description)),
                duedate=jira_issue.due_date,
                labels=jira_issue.labels,
                parent=JiraIssueParent(key=jira_issue.parent_issue)
                if jira_issue.parent_issue
                else None,
                issuetype=JiraIssueType(id=issue_type.id),
                priority=JiraIssuePriority(id=issue_priority.id),
                reporter=issue_reporter,
                project=JiraIssueProject(id=issue_project.id),
                summary=jira_issue.summary,
            )
        )

    async def get_matching_user_by_email(
        self,
        jira_user_email: str,
        jira_email: str,
        jira_api_token: str,
        jira_organization: str,
    ) -> JiraUser:
        response = await self.client.get(
            f"https://{jira_organization}.atlassian.net/rest/api/3/user/search?query={jira_user_email}",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        checked_response = self.check_response(response)
        jira_users = [JiraUser(**user) for user in self._parse_json(checked_response)]

        matching_users = [
            user
            for user in jira_users
            if user.emailAddress is not None
            and user.emailAddress.lower() == jira_user_email.lower()
        ]

        assert (
            len(matching_users) > 0
        ), f"No match user found for issue reporter email - {jira_user_email}"

        return matching_users[0]

    async def list_priorities(
        self,
        jira_email: str,
        jira_api_token: str,
        jira_organization: str,
    ) -> List[JiraIssuePriorityResponse]:
        response = await self.client.get(
            f"https://{jira_organization}.atlassian.net/rest/api/3/priority",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        checked_response = self.check_response(response)

        return [
            JiraIssuePriorityResponse(**priority)
            for priority in self._parse_json(checked_response)
        ]

    async def get_matching_priority(
        self,
        jira_priority: str,
        jira_email: str,
        jira_api_token: str,
        jira_organization: str,
    ) -> JiraIssuePriorityResponse:
        priorities = await self.list_priorities(
            jira_email,
            jira_api_token,
            jira_organization=jira_organization,
        )

        matching_priorities = [
            priority
            for priority in priorities
            if priority.name.lower() == jira_priority.lower()
        ]

        assert (
            len(matching_priorities) > 0
        ), f"No matching priority found for priority - {jira_priority}"

        return matching_priorities[0]

    async def get_jira_project(
        self,
        jira_project_name_or_id: str,
        jira_email: str,
        jira_api_token: str,
        jira_organization: str,
    ) -> JiraProject:
        response = await self.client.get(
            f"https://{jira_organization}.atlassian.net/rest/api/3/project/{jira_project_name_or_id}",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        checked_response = self.check_response(response)

        return JiraProject(**self._parse_json(checked_response))

    async def get_project_issue_types(
        self,
        project_id: str,
        jira_email: str,
        jira_api_token: str,
        jira_organization: str,
    ) -> List[JiraIssueTypeResponse]:
        response = await self.client.get(
            f"https://{jira_organization}.atlassian.net/rest/api/3/issuetype/project?projectId={project_id}",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        checked_response = self.check_response(response)

        return [
            JiraIssueTypeResponse(**issue_type)
            for issue_type in self._parse_json(checked_response)
        ]

    async def get_matching_project_issue_type(
        self,
        issue_type_name: str,
        project_id: str,
        jira_email: str,
        jira_api_token: str,
        jira_organization: str,
    ) -> JiraIssueTypeResponse:
        jira_issue_types = await self.get_project_issue_types(
            project_id,
            jira_email,
            jira_api_token,
            jira_organization=jira_organization,
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
        jira_organization: str,
    ) -> JiraIssueLinkTypes:
        response = await self.client.get(
            f"https://{jira_organization}.atlassian.net/rest/api/3/issueLinkType",
            auth=(
                jira_email,
                jira_api_token,
            ),
        )

        checked_response = self.check_response(response)

        return JiraIssueLinkTypes(**self._parse_json(checked_response))

    async def get_matching_issue_link_type(
        self,
        jira_issue_link_type: str,
        jira_email: str,
        jira_api_token: str,
        jira_organization: str,
    ) -> JiraIssueLinkType:
        link_types = await self.get_issue_link_types(
            jira_email,
            jira_api_token,
            jira_organization=jira_organization,
        )

        issue_link_types: list[JiraIssueLinkType] = link_types.issueLinkTypes
        target = jira_issue_link_type.lower()

        matching_link_types = [
            link_type
            for link_type in issue_link_types
            if link_type.inward.lower() == target
            or link_type.outward.lower() == target
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
        jira_organization: str,
    ) -> HTTPResponse:
        jira_link_type = await self.get_matching_issue_link_type(
            jira_issue_link_type,
            jira_email,
            jira_api_token,
            jira_organization=jira_organization,
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

        response = await self.client.post(
            f"https://{jira_organization}.atlassian.net/rest/api/3/issueLink",
            auth=(
                jira_email,
                jira_api_token,
            ),
            headers={"Content-Type": "application/json"},
            data=data.model_dump(mode="json", exclude_none=True),
        )

        return self.check_response(response)

    async def close(self) -> None:
        await self.client.close()

    def abort(self) -> None:
        self.client.abort()
