from __future__ import annotations

import asyncio
import datetime
import importlib
import re
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type

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


if TYPE_CHECKING:
    from .services.agents import AgentsService
    from .services.announcement_banner import AnnouncementBannerService
    from .services.app_data_policies import AppDataPoliciesService
    from .services.app_migration import AppMigrationService
    from .services.app_properties import AppPropertiesService
    from .services.application_roles import ApplicationRolesService
    from .services.audit_records import AuditRecordsService
    from .services.avatars import AvatarsService
    from .services.classification_levels import ClassificationLevelsService
    from .services.connect_to_forge_migration import ConnectToForgeMigrationService
    from .services.dashboards import DashboardsService
    from .services.dynamic_modules import DynamicModulesService
    from .services.field_schemes import FieldSchemesService
    from .services.filter_sharing import FilterSharingService
    from .services.filters import FiltersService
    from .services.group_and_user_picker import GroupAndUserPickerService
    from .services.groups import GroupsService
    from .services.issue_attachments import IssueAttachmentsService
    from .services.issue_bulk_operations import IssueBulkOperationsService
    from .services.issue_comment_properties import IssueCommentPropertiesService
    from .services.issue_comments import IssueCommentsService
    from .services.issue_custom_field_associations import IssueCustomFieldAssociationsService
    from .services.issue_custom_field_configuration_apps import IssueCustomFieldConfigurationAppsService
    from .services.issue_custom_field_contexts import IssueCustomFieldContextsService
    from .services.issue_custom_field_options import IssueCustomFieldOptionsService
    from .services.issue_custom_field_options_apps import IssueCustomFieldOptionsAppsService
    from .services.issue_custom_field_values_apps import IssueCustomFieldValuesAppsService
    from .services.issue_field_configurations import IssueFieldConfigurationsService
    from .services.issue_fields import IssueFieldsService
    from .services.issue_link_types import IssueLinkTypesService
    from .services.issue_links import IssueLinksService
    from .services.issue_navigator_settings import IssueNavigatorSettingsService
    from .services.issue_notification_schemes import IssueNotificationSchemesService
    from .services.issue_panels import IssuePanelsService
    from .services.issue_priorities import IssuePrioritiesService
    from .services.issue_properties import IssuePropertiesService
    from .services.issue_redaction import IssueRedactionService
    from .services.issue_remote_links import IssueRemoteLinksService
    from .services.issue_resolutions import IssueResolutionsService
    from .services.issue_search import IssueSearchService
    from .services.issue_security_level import IssueSecurityLevelService
    from .services.issue_security_schemes import IssueSecuritySchemesService
    from .services.issue_type_properties import IssueTypePropertiesService
    from .services.issue_type_schemes import IssueTypeSchemesService
    from .services.issue_type_screen_schemes import IssueTypeScreenSchemesService
    from .services.issue_types import IssueTypesService
    from .services.issue_votes import IssueVotesService
    from .services.issue_watchers import IssueWatchersService
    from .services.issue_worklog_properties import IssueWorklogPropertiesService
    from .services.issue_worklogs import IssueWorklogsService
    from .services.issues import IssuesService
    from .services.jira_expressions import JiraExpressionsService
    from .services.jira_settings import JiraSettingsService
    from .services.jql import JQLService
    from .services.jql_functions_apps import JQLFunctionsAppsService
    from .services.labels import LabelsService
    from .services.license_metrics import LicenseMetricsService
    from .services.myself import MyselfService
    from .services.permission_schemes import PermissionSchemesService
    from .services.permissions import PermissionsService
    from .services.plans import PlansService
    from .services.policies import PoliciesService
    from .services.priority_schemes import PrioritySchemesService
    from .services.project_avatars import ProjectAvatarsService
    from .services.project_categories import ProjectCategoriesService
    from .services.project_classification_levels import ProjectClassificationLevelsService
    from .services.project_components import ProjectComponentsService
    from .services.project_email import ProjectEmailService
    from .services.project_features import ProjectFeaturesService
    from .services.project_key_and_name_validation import ProjectKeyAndNameValidationService
    from .services.project_permission_schemes import ProjectPermissionSchemesService
    from .services.project_properties import ProjectPropertiesService
    from .services.project_role_actors import ProjectRoleActorsService
    from .services.project_roles import ProjectRolesService
    from .services.project_templates import ProjectTemplatesService
    from .services.project_types import ProjectTypesService
    from .services.project_versions import ProjectVersionsService
    from .services.projects import ProjectsService
    from .services.screen_schemes import ScreenSchemesService
    from .services.screen_tab_fields import ScreenTabFieldsService
    from .services.screen_tabs import ScreenTabsService
    from .services.screens import ScreensService
    from .services.server_info import ServerInfoService
    from .services.service_registry import ServiceRegistryService
    from .services.status import StatusService
    from .services.tasks import TasksService
    from .services.teams_in_plan import TeamsInPlanService
    from .services.time_tracking import TimeTrackingService
    from .services.ui_modifications_apps import UIModificationsAppsService
    from .services.user_properties import UserPropertiesService
    from .services.user_search import UserSearchService
    from .services.users import UsersService
    from .services.webhooks import WebhooksService
    from .services.workflow_scheme_drafts import WorkflowSchemeDraftsService
    from .services.workflow_scheme_project_associations import WorkflowSchemeProjectAssociationsService
    from .services.workflow_schemes import WorkflowSchemesService
    from .services.workflow_status_categories import WorkflowStatusCategoriesService
    from .services.workflow_statuses import WorkflowStatusesService
    from .services.workflow_transition_rules import WorkflowTransitionRulesService
    from .services.workflows import WorkflowsService

class Jira(Module):
    module_enabled = True
    dependencies = ["werkflow-http", "pydantic"]

    def __init__(
        self,
        organization: str | None = None,
        email: str | None = None,
        api_token: str | None = None,
    ) -> None:
        super().__init__()

        self.client = HTTP()
        self._organization: str | None = organization
        self._email: str | None = email
        self._api_token: str | None = api_token
        self._services: dict[str, Any] = {}

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

    def configure(
        self,
        organization: str,
        email: str,
        api_token: str,
    ) -> Jira:
        """Configure default Jira Cloud credentials used by all API v3 services."""
        self._organization = organization
        self._email = email
        self._api_token = api_token
        return self

    def _get_default_credentials(self) -> tuple[str | None, str | None, str | None]:
        return (self._organization, self._email, self._api_token)

    def _get_service(self, attr: str, module_name: str, class_name: str) -> Any:
        service = self._services.get(attr)
        if service is None:
            module = importlib.import_module(f".services.{module_name}", __package__)
            cls = getattr(module, class_name)
            service = cls(
                self.client,
                self.check_response,
                self._get_default_credentials,
            )
            self._services[attr] = service
        return service

    # --- Jira Cloud REST API v3 service properties (auto-generated) ---
    @property
    def agents(self) -> AgentsService:
        return self._get_service('agents', 'agents', 'AgentsService')

    @property
    def announcement_banner(self) -> AnnouncementBannerService:
        return self._get_service('announcement_banner', 'announcement_banner', 'AnnouncementBannerService')

    @property
    def app_data_policies(self) -> AppDataPoliciesService:
        return self._get_service('app_data_policies', 'app_data_policies', 'AppDataPoliciesService')

    @property
    def app_migration(self) -> AppMigrationService:
        return self._get_service('app_migration', 'app_migration', 'AppMigrationService')

    @property
    def app_properties(self) -> AppPropertiesService:
        return self._get_service('app_properties', 'app_properties', 'AppPropertiesService')

    @property
    def application_roles(self) -> ApplicationRolesService:
        return self._get_service('application_roles', 'application_roles', 'ApplicationRolesService')

    @property
    def audit_records(self) -> AuditRecordsService:
        return self._get_service('audit_records', 'audit_records', 'AuditRecordsService')

    @property
    def avatars(self) -> AvatarsService:
        return self._get_service('avatars', 'avatars', 'AvatarsService')

    @property
    def classification_levels(self) -> ClassificationLevelsService:
        return self._get_service('classification_levels', 'classification_levels', 'ClassificationLevelsService')

    @property
    def connect_to_forge_migration(self) -> ConnectToForgeMigrationService:
        return self._get_service('connect_to_forge_migration', 'connect_to_forge_migration', 'ConnectToForgeMigrationService')

    @property
    def dashboards(self) -> DashboardsService:
        return self._get_service('dashboards', 'dashboards', 'DashboardsService')

    @property
    def dynamic_modules(self) -> DynamicModulesService:
        return self._get_service('dynamic_modules', 'dynamic_modules', 'DynamicModulesService')

    @property
    def field_schemes(self) -> FieldSchemesService:
        return self._get_service('field_schemes', 'field_schemes', 'FieldSchemesService')

    @property
    def filter_sharing(self) -> FilterSharingService:
        return self._get_service('filter_sharing', 'filter_sharing', 'FilterSharingService')

    @property
    def filters(self) -> FiltersService:
        return self._get_service('filters', 'filters', 'FiltersService')

    @property
    def group_and_user_picker(self) -> GroupAndUserPickerService:
        return self._get_service('group_and_user_picker', 'group_and_user_picker', 'GroupAndUserPickerService')

    @property
    def groups(self) -> GroupsService:
        return self._get_service('groups', 'groups', 'GroupsService')

    @property
    def issue_attachments(self) -> IssueAttachmentsService:
        return self._get_service('issue_attachments', 'issue_attachments', 'IssueAttachmentsService')

    @property
    def issue_bulk_operations(self) -> IssueBulkOperationsService:
        return self._get_service('issue_bulk_operations', 'issue_bulk_operations', 'IssueBulkOperationsService')

    @property
    def issue_comment_properties(self) -> IssueCommentPropertiesService:
        return self._get_service('issue_comment_properties', 'issue_comment_properties', 'IssueCommentPropertiesService')

    @property
    def issue_comments(self) -> IssueCommentsService:
        return self._get_service('issue_comments', 'issue_comments', 'IssueCommentsService')

    @property
    def issue_custom_field_associations(self) -> IssueCustomFieldAssociationsService:
        return self._get_service('issue_custom_field_associations', 'issue_custom_field_associations', 'IssueCustomFieldAssociationsService')

    @property
    def issue_custom_field_configuration_apps(self) -> IssueCustomFieldConfigurationAppsService:
        return self._get_service('issue_custom_field_configuration_apps', 'issue_custom_field_configuration_apps', 'IssueCustomFieldConfigurationAppsService')

    @property
    def issue_custom_field_contexts(self) -> IssueCustomFieldContextsService:
        return self._get_service('issue_custom_field_contexts', 'issue_custom_field_contexts', 'IssueCustomFieldContextsService')

    @property
    def issue_custom_field_options(self) -> IssueCustomFieldOptionsService:
        return self._get_service('issue_custom_field_options', 'issue_custom_field_options', 'IssueCustomFieldOptionsService')

    @property
    def issue_custom_field_options_apps(self) -> IssueCustomFieldOptionsAppsService:
        return self._get_service('issue_custom_field_options_apps', 'issue_custom_field_options_apps', 'IssueCustomFieldOptionsAppsService')

    @property
    def issue_custom_field_values_apps(self) -> IssueCustomFieldValuesAppsService:
        return self._get_service('issue_custom_field_values_apps', 'issue_custom_field_values_apps', 'IssueCustomFieldValuesAppsService')

    @property
    def issue_field_configurations(self) -> IssueFieldConfigurationsService:
        return self._get_service('issue_field_configurations', 'issue_field_configurations', 'IssueFieldConfigurationsService')

    @property
    def issue_fields(self) -> IssueFieldsService:
        return self._get_service('issue_fields', 'issue_fields', 'IssueFieldsService')

    @property
    def issue_link_types(self) -> IssueLinkTypesService:
        return self._get_service('issue_link_types', 'issue_link_types', 'IssueLinkTypesService')

    @property
    def issue_links(self) -> IssueLinksService:
        return self._get_service('issue_links', 'issue_links', 'IssueLinksService')

    @property
    def issue_navigator_settings(self) -> IssueNavigatorSettingsService:
        return self._get_service('issue_navigator_settings', 'issue_navigator_settings', 'IssueNavigatorSettingsService')

    @property
    def issue_notification_schemes(self) -> IssueNotificationSchemesService:
        return self._get_service('issue_notification_schemes', 'issue_notification_schemes', 'IssueNotificationSchemesService')

    @property
    def issue_panels(self) -> IssuePanelsService:
        return self._get_service('issue_panels', 'issue_panels', 'IssuePanelsService')

    @property
    def issue_priorities(self) -> IssuePrioritiesService:
        return self._get_service('issue_priorities', 'issue_priorities', 'IssuePrioritiesService')

    @property
    def issue_properties(self) -> IssuePropertiesService:
        return self._get_service('issue_properties', 'issue_properties', 'IssuePropertiesService')

    @property
    def issue_redaction(self) -> IssueRedactionService:
        return self._get_service('issue_redaction', 'issue_redaction', 'IssueRedactionService')

    @property
    def issue_remote_links(self) -> IssueRemoteLinksService:
        return self._get_service('issue_remote_links', 'issue_remote_links', 'IssueRemoteLinksService')

    @property
    def issue_resolutions(self) -> IssueResolutionsService:
        return self._get_service('issue_resolutions', 'issue_resolutions', 'IssueResolutionsService')

    @property
    def issue_search(self) -> IssueSearchService:
        return self._get_service('issue_search', 'issue_search', 'IssueSearchService')

    @property
    def issue_security_level(self) -> IssueSecurityLevelService:
        return self._get_service('issue_security_level', 'issue_security_level', 'IssueSecurityLevelService')

    @property
    def issue_security_schemes(self) -> IssueSecuritySchemesService:
        return self._get_service('issue_security_schemes', 'issue_security_schemes', 'IssueSecuritySchemesService')

    @property
    def issue_type_properties(self) -> IssueTypePropertiesService:
        return self._get_service('issue_type_properties', 'issue_type_properties', 'IssueTypePropertiesService')

    @property
    def issue_type_schemes(self) -> IssueTypeSchemesService:
        return self._get_service('issue_type_schemes', 'issue_type_schemes', 'IssueTypeSchemesService')

    @property
    def issue_type_screen_schemes(self) -> IssueTypeScreenSchemesService:
        return self._get_service('issue_type_screen_schemes', 'issue_type_screen_schemes', 'IssueTypeScreenSchemesService')

    @property
    def issue_types(self) -> IssueTypesService:
        return self._get_service('issue_types', 'issue_types', 'IssueTypesService')

    @property
    def issue_votes(self) -> IssueVotesService:
        return self._get_service('issue_votes', 'issue_votes', 'IssueVotesService')

    @property
    def issue_watchers(self) -> IssueWatchersService:
        return self._get_service('issue_watchers', 'issue_watchers', 'IssueWatchersService')

    @property
    def issue_worklog_properties(self) -> IssueWorklogPropertiesService:
        return self._get_service('issue_worklog_properties', 'issue_worklog_properties', 'IssueWorklogPropertiesService')

    @property
    def issue_worklogs(self) -> IssueWorklogsService:
        return self._get_service('issue_worklogs', 'issue_worklogs', 'IssueWorklogsService')

    @property
    def issues(self) -> IssuesService:
        return self._get_service('issues', 'issues', 'IssuesService')

    @property
    def jira_expressions(self) -> JiraExpressionsService:
        return self._get_service('jira_expressions', 'jira_expressions', 'JiraExpressionsService')

    @property
    def jira_settings(self) -> JiraSettingsService:
        return self._get_service('jira_settings', 'jira_settings', 'JiraSettingsService')

    @property
    def jql(self) -> JQLService:
        return self._get_service('jql', 'jql', 'JQLService')

    @property
    def jql_functions_apps(self) -> JQLFunctionsAppsService:
        return self._get_service('jql_functions_apps', 'jql_functions_apps', 'JQLFunctionsAppsService')

    @property
    def labels(self) -> LabelsService:
        return self._get_service('labels', 'labels', 'LabelsService')

    @property
    def license_metrics(self) -> LicenseMetricsService:
        return self._get_service('license_metrics', 'license_metrics', 'LicenseMetricsService')

    @property
    def myself(self) -> MyselfService:
        return self._get_service('myself', 'myself', 'MyselfService')

    @property
    def permission_schemes(self) -> PermissionSchemesService:
        return self._get_service('permission_schemes', 'permission_schemes', 'PermissionSchemesService')

    @property
    def permissions(self) -> PermissionsService:
        return self._get_service('permissions', 'permissions', 'PermissionsService')

    @property
    def plans(self) -> PlansService:
        return self._get_service('plans', 'plans', 'PlansService')

    @property
    def policies(self) -> PoliciesService:
        return self._get_service('policies', 'policies', 'PoliciesService')

    @property
    def priority_schemes(self) -> PrioritySchemesService:
        return self._get_service('priority_schemes', 'priority_schemes', 'PrioritySchemesService')

    @property
    def project_avatars(self) -> ProjectAvatarsService:
        return self._get_service('project_avatars', 'project_avatars', 'ProjectAvatarsService')

    @property
    def project_categories(self) -> ProjectCategoriesService:
        return self._get_service('project_categories', 'project_categories', 'ProjectCategoriesService')

    @property
    def project_classification_levels(self) -> ProjectClassificationLevelsService:
        return self._get_service('project_classification_levels', 'project_classification_levels', 'ProjectClassificationLevelsService')

    @property
    def project_components(self) -> ProjectComponentsService:
        return self._get_service('project_components', 'project_components', 'ProjectComponentsService')

    @property
    def project_email(self) -> ProjectEmailService:
        return self._get_service('project_email', 'project_email', 'ProjectEmailService')

    @property
    def project_features(self) -> ProjectFeaturesService:
        return self._get_service('project_features', 'project_features', 'ProjectFeaturesService')

    @property
    def project_key_and_name_validation(self) -> ProjectKeyAndNameValidationService:
        return self._get_service('project_key_and_name_validation', 'project_key_and_name_validation', 'ProjectKeyAndNameValidationService')

    @property
    def project_permission_schemes(self) -> ProjectPermissionSchemesService:
        return self._get_service('project_permission_schemes', 'project_permission_schemes', 'ProjectPermissionSchemesService')

    @property
    def project_properties(self) -> ProjectPropertiesService:
        return self._get_service('project_properties', 'project_properties', 'ProjectPropertiesService')

    @property
    def project_role_actors(self) -> ProjectRoleActorsService:
        return self._get_service('project_role_actors', 'project_role_actors', 'ProjectRoleActorsService')

    @property
    def project_roles(self) -> ProjectRolesService:
        return self._get_service('project_roles', 'project_roles', 'ProjectRolesService')

    @property
    def project_templates(self) -> ProjectTemplatesService:
        return self._get_service('project_templates', 'project_templates', 'ProjectTemplatesService')

    @property
    def project_types(self) -> ProjectTypesService:
        return self._get_service('project_types', 'project_types', 'ProjectTypesService')

    @property
    def project_versions(self) -> ProjectVersionsService:
        return self._get_service('project_versions', 'project_versions', 'ProjectVersionsService')

    @property
    def projects(self) -> ProjectsService:
        return self._get_service('projects', 'projects', 'ProjectsService')

    @property
    def screen_schemes(self) -> ScreenSchemesService:
        return self._get_service('screen_schemes', 'screen_schemes', 'ScreenSchemesService')

    @property
    def screen_tab_fields(self) -> ScreenTabFieldsService:
        return self._get_service('screen_tab_fields', 'screen_tab_fields', 'ScreenTabFieldsService')

    @property
    def screen_tabs(self) -> ScreenTabsService:
        return self._get_service('screen_tabs', 'screen_tabs', 'ScreenTabsService')

    @property
    def screens(self) -> ScreensService:
        return self._get_service('screens', 'screens', 'ScreensService')

    @property
    def server_info(self) -> ServerInfoService:
        return self._get_service('server_info', 'server_info', 'ServerInfoService')

    @property
    def service_registry(self) -> ServiceRegistryService:
        return self._get_service('service_registry', 'service_registry', 'ServiceRegistryService')

    @property
    def status(self) -> StatusService:
        return self._get_service('status', 'status', 'StatusService')

    @property
    def tasks(self) -> TasksService:
        return self._get_service('tasks', 'tasks', 'TasksService')

    @property
    def teams_in_plan(self) -> TeamsInPlanService:
        return self._get_service('teams_in_plan', 'teams_in_plan', 'TeamsInPlanService')

    @property
    def time_tracking(self) -> TimeTrackingService:
        return self._get_service('time_tracking', 'time_tracking', 'TimeTrackingService')

    @property
    def ui_modifications_apps(self) -> UIModificationsAppsService:
        return self._get_service('ui_modifications_apps', 'ui_modifications_apps', 'UIModificationsAppsService')

    @property
    def user_properties(self) -> UserPropertiesService:
        return self._get_service('user_properties', 'user_properties', 'UserPropertiesService')

    @property
    def user_search(self) -> UserSearchService:
        return self._get_service('user_search', 'user_search', 'UserSearchService')

    @property
    def users(self) -> UsersService:
        return self._get_service('users', 'users', 'UsersService')

    @property
    def webhooks(self) -> WebhooksService:
        return self._get_service('webhooks', 'webhooks', 'WebhooksService')

    @property
    def workflow_scheme_drafts(self) -> WorkflowSchemeDraftsService:
        return self._get_service('workflow_scheme_drafts', 'workflow_scheme_drafts', 'WorkflowSchemeDraftsService')

    @property
    def workflow_scheme_project_associations(self) -> WorkflowSchemeProjectAssociationsService:
        return self._get_service('workflow_scheme_project_associations', 'workflow_scheme_project_associations', 'WorkflowSchemeProjectAssociationsService')

    @property
    def workflow_schemes(self) -> WorkflowSchemesService:
        return self._get_service('workflow_schemes', 'workflow_schemes', 'WorkflowSchemesService')

    @property
    def workflow_status_categories(self) -> WorkflowStatusCategoriesService:
        return self._get_service('workflow_status_categories', 'workflow_status_categories', 'WorkflowStatusCategoriesService')

    @property
    def workflow_statuses(self) -> WorkflowStatusesService:
        return self._get_service('workflow_statuses', 'workflow_statuses', 'WorkflowStatusesService')

    @property
    def workflow_transition_rules(self) -> WorkflowTransitionRulesService:
        return self._get_service('workflow_transition_rules', 'workflow_transition_rules', 'WorkflowTransitionRulesService')

    @property
    def workflows(self) -> WorkflowsService:
        return self._get_service('workflows', 'workflows', 'WorkflowsService')
