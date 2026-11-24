from .content import (
    BackgroundColorMarkAttrs as BackgroundColorMarkAttrs,
    EmojiAttrs as EmojiAttrs,
    EmojirAttrs as EmojirAttrs,
    HardBreakAttrs as HardBreakAttrs,
    HeadingAttrs as HeadingAttrs,
    InlineCardAttrs as InlineCardAttrs,
    JiraChildBlock as JiraChildBlock,
    JiraContentMark as JiraContentMark,
    JiraInlineBlock as JiraInlineBlock,
    JiraTopLevelBlock as JiraTopLevelBlock,
    LinkMarkAttrs as LinkMarkAttrs,
    MediaAttrs as MediaAttrs,
    MediaSingleAttrs as MediaSingleAttrs,
    MentionAttrs as MentionAttrs,
    OrderedListAttrs as OrderedListAttrs,
    PanelAttrs as PanelAttrs,
    ParagraphAttrs as ParagraphAttrs,
    SubSupMarkAttrs as SubSupMarkAttrs,
    TableAttrs as TableAttrs,
    TableCellAttrs as TableCellAttrs,
    TableHeaderAttrs as TableHeaderAttrs,
    TextColorAttrs as TextColorAttrs,
)
from .jira import Jira as Jira
from .models import (
    BadRequestError as BadRequestError,
    Issue as Issue,
    JiraIssue as JiraIssue,
    JiraIssueAssignee as JiraIssueAssignee,
    JiraIssueBatch as JiraIssueBatch,
    JiraIssueDescription as JiraIssueDescription,
    JiraIssueFields as JiraIssueFields,
    JiraIssueLink as JiraIssueLink,
    JiraIssueLinkComment as JiraIssueLinkComment,
    JiraIssueLinkKey as JiraIssueLinkKey,
    JiraIssueLinkRefType as JiraIssueLinkRefType,
    JiraIssueLinkType as JiraIssueLinkType,
    JiraIssueLinkTypes as JiraIssueLinkTypes,
    JiraIssueParent as JiraIssueParent,
    JiraIssuePriority as JiraIssuePriority,
    JiraIssuePriorityResponse as JiraIssuePriorityResponse,
    JiraIssueProject as JiraIssueProject,
    JiraIssueReporter as JiraIssueReporter,
    JiraIssueResponse as JiraIssueResponse,
    JiraIssueType as JiraIssueType,
    JiraIssueTypeResponse as JiraIssueTypeResponse,
    JiraProject as JiraProject,
    JiraUser as JiraUser,
    MethodNotAllowedError as MethodNotAllowedError,
    ResourceNotFoundError as ResourceNotFoundError,
    ServerFailedError as ServerFailedError,
    UnauthorizedRequestError as UnauthorizedRequestError,
    UnprocessableContentError as UnprocessableContentError,
)

import importlib as _importlib
from typing import TYPE_CHECKING as _TYPE_CHECKING, Any as _Any

from .services.base import JiraBaseService as JiraBaseService

if _TYPE_CHECKING:
    from .services.agents import AgentsService as AgentsService
    from .services.announcement_banner import AnnouncementBannerService as AnnouncementBannerService
    from .services.app_data_policies import AppDataPoliciesService as AppDataPoliciesService
    from .services.app_migration import AppMigrationService as AppMigrationService
    from .services.app_properties import AppPropertiesService as AppPropertiesService
    from .services.application_roles import ApplicationRolesService as ApplicationRolesService
    from .services.audit_records import AuditRecordsService as AuditRecordsService
    from .services.avatars import AvatarsService as AvatarsService
    from .services.classification_levels import ClassificationLevelsService as ClassificationLevelsService
    from .services.connect_to_forge_migration import ConnectToForgeMigrationService as ConnectToForgeMigrationService
    from .services.dashboards import DashboardsService as DashboardsService
    from .services.dynamic_modules import DynamicModulesService as DynamicModulesService
    from .services.field_schemes import FieldSchemesService as FieldSchemesService
    from .services.filter_sharing import FilterSharingService as FilterSharingService
    from .services.filters import FiltersService as FiltersService
    from .services.group_and_user_picker import GroupAndUserPickerService as GroupAndUserPickerService
    from .services.groups import GroupsService as GroupsService
    from .services.issue_attachments import IssueAttachmentsService as IssueAttachmentsService
    from .services.issue_bulk_operations import IssueBulkOperationsService as IssueBulkOperationsService
    from .services.issue_comment_properties import IssueCommentPropertiesService as IssueCommentPropertiesService
    from .services.issue_comments import IssueCommentsService as IssueCommentsService
    from .services.issue_custom_field_associations import IssueCustomFieldAssociationsService as IssueCustomFieldAssociationsService
    from .services.issue_custom_field_configuration_apps import IssueCustomFieldConfigurationAppsService as IssueCustomFieldConfigurationAppsService
    from .services.issue_custom_field_contexts import IssueCustomFieldContextsService as IssueCustomFieldContextsService
    from .services.issue_custom_field_options import IssueCustomFieldOptionsService as IssueCustomFieldOptionsService
    from .services.issue_custom_field_options_apps import IssueCustomFieldOptionsAppsService as IssueCustomFieldOptionsAppsService
    from .services.issue_custom_field_values_apps import IssueCustomFieldValuesAppsService as IssueCustomFieldValuesAppsService
    from .services.issue_field_configurations import IssueFieldConfigurationsService as IssueFieldConfigurationsService
    from .services.issue_fields import IssueFieldsService as IssueFieldsService
    from .services.issue_link_types import IssueLinkTypesService as IssueLinkTypesService
    from .services.issue_links import IssueLinksService as IssueLinksService
    from .services.issue_navigator_settings import IssueNavigatorSettingsService as IssueNavigatorSettingsService
    from .services.issue_notification_schemes import IssueNotificationSchemesService as IssueNotificationSchemesService
    from .services.issue_panels import IssuePanelsService as IssuePanelsService
    from .services.issue_priorities import IssuePrioritiesService as IssuePrioritiesService
    from .services.issue_properties import IssuePropertiesService as IssuePropertiesService
    from .services.issue_redaction import IssueRedactionService as IssueRedactionService
    from .services.issue_remote_links import IssueRemoteLinksService as IssueRemoteLinksService
    from .services.issue_resolutions import IssueResolutionsService as IssueResolutionsService
    from .services.issue_search import IssueSearchService as IssueSearchService
    from .services.issue_security_level import IssueSecurityLevelService as IssueSecurityLevelService
    from .services.issue_security_schemes import IssueSecuritySchemesService as IssueSecuritySchemesService
    from .services.issue_type_properties import IssueTypePropertiesService as IssueTypePropertiesService
    from .services.issue_type_schemes import IssueTypeSchemesService as IssueTypeSchemesService
    from .services.issue_type_screen_schemes import IssueTypeScreenSchemesService as IssueTypeScreenSchemesService
    from .services.issue_types import IssueTypesService as IssueTypesService
    from .services.issue_votes import IssueVotesService as IssueVotesService
    from .services.issue_watchers import IssueWatchersService as IssueWatchersService
    from .services.issue_worklog_properties import IssueWorklogPropertiesService as IssueWorklogPropertiesService
    from .services.issue_worklogs import IssueWorklogsService as IssueWorklogsService
    from .services.issues import IssuesService as IssuesService
    from .services.jira_expressions import JiraExpressionsService as JiraExpressionsService
    from .services.jira_settings import JiraSettingsService as JiraSettingsService
    from .services.jql import JQLService as JQLService
    from .services.jql_functions_apps import JQLFunctionsAppsService as JQLFunctionsAppsService
    from .services.labels import LabelsService as LabelsService
    from .services.license_metrics import LicenseMetricsService as LicenseMetricsService
    from .services.myself import MyselfService as MyselfService
    from .services.permission_schemes import PermissionSchemesService as PermissionSchemesService
    from .services.permissions import PermissionsService as PermissionsService
    from .services.plans import PlansService as PlansService
    from .services.policies import PoliciesService as PoliciesService
    from .services.priority_schemes import PrioritySchemesService as PrioritySchemesService
    from .services.project_avatars import ProjectAvatarsService as ProjectAvatarsService
    from .services.project_categories import ProjectCategoriesService as ProjectCategoriesService
    from .services.project_classification_levels import ProjectClassificationLevelsService as ProjectClassificationLevelsService
    from .services.project_components import ProjectComponentsService as ProjectComponentsService
    from .services.project_email import ProjectEmailService as ProjectEmailService
    from .services.project_features import ProjectFeaturesService as ProjectFeaturesService
    from .services.project_key_and_name_validation import ProjectKeyAndNameValidationService as ProjectKeyAndNameValidationService
    from .services.project_permission_schemes import ProjectPermissionSchemesService as ProjectPermissionSchemesService
    from .services.project_properties import ProjectPropertiesService as ProjectPropertiesService
    from .services.project_role_actors import ProjectRoleActorsService as ProjectRoleActorsService
    from .services.project_roles import ProjectRolesService as ProjectRolesService
    from .services.project_templates import ProjectTemplatesService as ProjectTemplatesService
    from .services.project_types import ProjectTypesService as ProjectTypesService
    from .services.project_versions import ProjectVersionsService as ProjectVersionsService
    from .services.projects import ProjectsService as ProjectsService
    from .services.screen_schemes import ScreenSchemesService as ScreenSchemesService
    from .services.screen_tab_fields import ScreenTabFieldsService as ScreenTabFieldsService
    from .services.screen_tabs import ScreenTabsService as ScreenTabsService
    from .services.screens import ScreensService as ScreensService
    from .services.server_info import ServerInfoService as ServerInfoService
    from .services.service_registry import ServiceRegistryService as ServiceRegistryService
    from .services.status import StatusService as StatusService
    from .services.tasks import TasksService as TasksService
    from .services.teams_in_plan import TeamsInPlanService as TeamsInPlanService
    from .services.time_tracking import TimeTrackingService as TimeTrackingService
    from .services.ui_modifications_apps import UIModificationsAppsService as UIModificationsAppsService
    from .services.user_properties import UserPropertiesService as UserPropertiesService
    from .services.user_search import UserSearchService as UserSearchService
    from .services.users import UsersService as UsersService
    from .services.webhooks import WebhooksService as WebhooksService
    from .services.workflow_scheme_drafts import WorkflowSchemeDraftsService as WorkflowSchemeDraftsService
    from .services.workflow_scheme_project_associations import WorkflowSchemeProjectAssociationsService as WorkflowSchemeProjectAssociationsService
    from .services.workflow_schemes import WorkflowSchemesService as WorkflowSchemesService
    from .services.workflow_status_categories import WorkflowStatusCategoriesService as WorkflowStatusCategoriesService
    from .services.workflow_statuses import WorkflowStatusesService as WorkflowStatusesService
    from .services.workflow_transition_rules import WorkflowTransitionRulesService as WorkflowTransitionRulesService
    from .services.workflows import WorkflowsService as WorkflowsService

_LAZY_SERVICE_EXPORTS: dict[str, tuple[str, str]] = {
    "AgentsService": (".services.agents", "AgentsService"),
    "AnnouncementBannerService": (".services.announcement_banner", "AnnouncementBannerService"),
    "AppDataPoliciesService": (".services.app_data_policies", "AppDataPoliciesService"),
    "AppMigrationService": (".services.app_migration", "AppMigrationService"),
    "AppPropertiesService": (".services.app_properties", "AppPropertiesService"),
    "ApplicationRolesService": (".services.application_roles", "ApplicationRolesService"),
    "AuditRecordsService": (".services.audit_records", "AuditRecordsService"),
    "AvatarsService": (".services.avatars", "AvatarsService"),
    "ClassificationLevelsService": (".services.classification_levels", "ClassificationLevelsService"),
    "ConnectToForgeMigrationService": (".services.connect_to_forge_migration", "ConnectToForgeMigrationService"),
    "DashboardsService": (".services.dashboards", "DashboardsService"),
    "DynamicModulesService": (".services.dynamic_modules", "DynamicModulesService"),
    "FieldSchemesService": (".services.field_schemes", "FieldSchemesService"),
    "FilterSharingService": (".services.filter_sharing", "FilterSharingService"),
    "FiltersService": (".services.filters", "FiltersService"),
    "GroupAndUserPickerService": (".services.group_and_user_picker", "GroupAndUserPickerService"),
    "GroupsService": (".services.groups", "GroupsService"),
    "IssueAttachmentsService": (".services.issue_attachments", "IssueAttachmentsService"),
    "IssueBulkOperationsService": (".services.issue_bulk_operations", "IssueBulkOperationsService"),
    "IssueCommentPropertiesService": (".services.issue_comment_properties", "IssueCommentPropertiesService"),
    "IssueCommentsService": (".services.issue_comments", "IssueCommentsService"),
    "IssueCustomFieldAssociationsService": (".services.issue_custom_field_associations", "IssueCustomFieldAssociationsService"),
    "IssueCustomFieldConfigurationAppsService": (".services.issue_custom_field_configuration_apps", "IssueCustomFieldConfigurationAppsService"),
    "IssueCustomFieldContextsService": (".services.issue_custom_field_contexts", "IssueCustomFieldContextsService"),
    "IssueCustomFieldOptionsService": (".services.issue_custom_field_options", "IssueCustomFieldOptionsService"),
    "IssueCustomFieldOptionsAppsService": (".services.issue_custom_field_options_apps", "IssueCustomFieldOptionsAppsService"),
    "IssueCustomFieldValuesAppsService": (".services.issue_custom_field_values_apps", "IssueCustomFieldValuesAppsService"),
    "IssueFieldConfigurationsService": (".services.issue_field_configurations", "IssueFieldConfigurationsService"),
    "IssueFieldsService": (".services.issue_fields", "IssueFieldsService"),
    "IssueLinkTypesService": (".services.issue_link_types", "IssueLinkTypesService"),
    "IssueLinksService": (".services.issue_links", "IssueLinksService"),
    "IssueNavigatorSettingsService": (".services.issue_navigator_settings", "IssueNavigatorSettingsService"),
    "IssueNotificationSchemesService": (".services.issue_notification_schemes", "IssueNotificationSchemesService"),
    "IssuePanelsService": (".services.issue_panels", "IssuePanelsService"),
    "IssuePrioritiesService": (".services.issue_priorities", "IssuePrioritiesService"),
    "IssuePropertiesService": (".services.issue_properties", "IssuePropertiesService"),
    "IssueRedactionService": (".services.issue_redaction", "IssueRedactionService"),
    "IssueRemoteLinksService": (".services.issue_remote_links", "IssueRemoteLinksService"),
    "IssueResolutionsService": (".services.issue_resolutions", "IssueResolutionsService"),
    "IssueSearchService": (".services.issue_search", "IssueSearchService"),
    "IssueSecurityLevelService": (".services.issue_security_level", "IssueSecurityLevelService"),
    "IssueSecuritySchemesService": (".services.issue_security_schemes", "IssueSecuritySchemesService"),
    "IssueTypePropertiesService": (".services.issue_type_properties", "IssueTypePropertiesService"),
    "IssueTypeSchemesService": (".services.issue_type_schemes", "IssueTypeSchemesService"),
    "IssueTypeScreenSchemesService": (".services.issue_type_screen_schemes", "IssueTypeScreenSchemesService"),
    "IssueTypesService": (".services.issue_types", "IssueTypesService"),
    "IssueVotesService": (".services.issue_votes", "IssueVotesService"),
    "IssueWatchersService": (".services.issue_watchers", "IssueWatchersService"),
    "IssueWorklogPropertiesService": (".services.issue_worklog_properties", "IssueWorklogPropertiesService"),
    "IssueWorklogsService": (".services.issue_worklogs", "IssueWorklogsService"),
    "IssuesService": (".services.issues", "IssuesService"),
    "JiraExpressionsService": (".services.jira_expressions", "JiraExpressionsService"),
    "JiraSettingsService": (".services.jira_settings", "JiraSettingsService"),
    "JQLService": (".services.jql", "JQLService"),
    "JQLFunctionsAppsService": (".services.jql_functions_apps", "JQLFunctionsAppsService"),
    "LabelsService": (".services.labels", "LabelsService"),
    "LicenseMetricsService": (".services.license_metrics", "LicenseMetricsService"),
    "MyselfService": (".services.myself", "MyselfService"),
    "PermissionSchemesService": (".services.permission_schemes", "PermissionSchemesService"),
    "PermissionsService": (".services.permissions", "PermissionsService"),
    "PlansService": (".services.plans", "PlansService"),
    "PoliciesService": (".services.policies", "PoliciesService"),
    "PrioritySchemesService": (".services.priority_schemes", "PrioritySchemesService"),
    "ProjectAvatarsService": (".services.project_avatars", "ProjectAvatarsService"),
    "ProjectCategoriesService": (".services.project_categories", "ProjectCategoriesService"),
    "ProjectClassificationLevelsService": (".services.project_classification_levels", "ProjectClassificationLevelsService"),
    "ProjectComponentsService": (".services.project_components", "ProjectComponentsService"),
    "ProjectEmailService": (".services.project_email", "ProjectEmailService"),
    "ProjectFeaturesService": (".services.project_features", "ProjectFeaturesService"),
    "ProjectKeyAndNameValidationService": (".services.project_key_and_name_validation", "ProjectKeyAndNameValidationService"),
    "ProjectPermissionSchemesService": (".services.project_permission_schemes", "ProjectPermissionSchemesService"),
    "ProjectPropertiesService": (".services.project_properties", "ProjectPropertiesService"),
    "ProjectRoleActorsService": (".services.project_role_actors", "ProjectRoleActorsService"),
    "ProjectRolesService": (".services.project_roles", "ProjectRolesService"),
    "ProjectTemplatesService": (".services.project_templates", "ProjectTemplatesService"),
    "ProjectTypesService": (".services.project_types", "ProjectTypesService"),
    "ProjectVersionsService": (".services.project_versions", "ProjectVersionsService"),
    "ProjectsService": (".services.projects", "ProjectsService"),
    "ScreenSchemesService": (".services.screen_schemes", "ScreenSchemesService"),
    "ScreenTabFieldsService": (".services.screen_tab_fields", "ScreenTabFieldsService"),
    "ScreenTabsService": (".services.screen_tabs", "ScreenTabsService"),
    "ScreensService": (".services.screens", "ScreensService"),
    "ServerInfoService": (".services.server_info", "ServerInfoService"),
    "ServiceRegistryService": (".services.service_registry", "ServiceRegistryService"),
    "StatusService": (".services.status", "StatusService"),
    "TasksService": (".services.tasks", "TasksService"),
    "TeamsInPlanService": (".services.teams_in_plan", "TeamsInPlanService"),
    "TimeTrackingService": (".services.time_tracking", "TimeTrackingService"),
    "UIModificationsAppsService": (".services.ui_modifications_apps", "UIModificationsAppsService"),
    "UserPropertiesService": (".services.user_properties", "UserPropertiesService"),
    "UserSearchService": (".services.user_search", "UserSearchService"),
    "UsersService": (".services.users", "UsersService"),
    "WebhooksService": (".services.webhooks", "WebhooksService"),
    "WorkflowSchemeDraftsService": (".services.workflow_scheme_drafts", "WorkflowSchemeDraftsService"),
    "WorkflowSchemeProjectAssociationsService": (".services.workflow_scheme_project_associations", "WorkflowSchemeProjectAssociationsService"),
    "WorkflowSchemesService": (".services.workflow_schemes", "WorkflowSchemesService"),
    "WorkflowStatusCategoriesService": (".services.workflow_status_categories", "WorkflowStatusCategoriesService"),
    "WorkflowStatusesService": (".services.workflow_statuses", "WorkflowStatusesService"),
    "WorkflowTransitionRulesService": (".services.workflow_transition_rules", "WorkflowTransitionRulesService"),
    "WorkflowsService": (".services.workflows", "WorkflowsService"),
}

def __getattr__(name: str) -> _Any:
    if name in _LAZY_SERVICE_EXPORTS:
        module_path, attr = _LAZY_SERVICE_EXPORTS[name]
        module = _importlib.import_module(module_path, __name__)
        value = getattr(module, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
