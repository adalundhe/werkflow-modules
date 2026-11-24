from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

from .base import JiraBaseService as JiraBaseService

if TYPE_CHECKING:
    from .agents import AgentsService as AgentsService
    from .announcement_banner import AnnouncementBannerService as AnnouncementBannerService
    from .app_data_policies import AppDataPoliciesService as AppDataPoliciesService
    from .app_migration import AppMigrationService as AppMigrationService
    from .app_properties import AppPropertiesService as AppPropertiesService
    from .application_roles import ApplicationRolesService as ApplicationRolesService
    from .audit_records import AuditRecordsService as AuditRecordsService
    from .avatars import AvatarsService as AvatarsService
    from .classification_levels import ClassificationLevelsService as ClassificationLevelsService
    from .connect_to_forge_migration import ConnectToForgeMigrationService as ConnectToForgeMigrationService
    from .dashboards import DashboardsService as DashboardsService
    from .dynamic_modules import DynamicModulesService as DynamicModulesService
    from .field_schemes import FieldSchemesService as FieldSchemesService
    from .filter_sharing import FilterSharingService as FilterSharingService
    from .filters import FiltersService as FiltersService
    from .group_and_user_picker import GroupAndUserPickerService as GroupAndUserPickerService
    from .groups import GroupsService as GroupsService
    from .issue_attachments import IssueAttachmentsService as IssueAttachmentsService
    from .issue_bulk_operations import IssueBulkOperationsService as IssueBulkOperationsService
    from .issue_comment_properties import IssueCommentPropertiesService as IssueCommentPropertiesService
    from .issue_comments import IssueCommentsService as IssueCommentsService
    from .issue_custom_field_associations import IssueCustomFieldAssociationsService as IssueCustomFieldAssociationsService
    from .issue_custom_field_configuration_apps import IssueCustomFieldConfigurationAppsService as IssueCustomFieldConfigurationAppsService
    from .issue_custom_field_contexts import IssueCustomFieldContextsService as IssueCustomFieldContextsService
    from .issue_custom_field_options import IssueCustomFieldOptionsService as IssueCustomFieldOptionsService
    from .issue_custom_field_options_apps import IssueCustomFieldOptionsAppsService as IssueCustomFieldOptionsAppsService
    from .issue_custom_field_values_apps import IssueCustomFieldValuesAppsService as IssueCustomFieldValuesAppsService
    from .issue_field_configurations import IssueFieldConfigurationsService as IssueFieldConfigurationsService
    from .issue_fields import IssueFieldsService as IssueFieldsService
    from .issue_link_types import IssueLinkTypesService as IssueLinkTypesService
    from .issue_links import IssueLinksService as IssueLinksService
    from .issue_navigator_settings import IssueNavigatorSettingsService as IssueNavigatorSettingsService
    from .issue_notification_schemes import IssueNotificationSchemesService as IssueNotificationSchemesService
    from .issue_panels import IssuePanelsService as IssuePanelsService
    from .issue_priorities import IssuePrioritiesService as IssuePrioritiesService
    from .issue_properties import IssuePropertiesService as IssuePropertiesService
    from .issue_redaction import IssueRedactionService as IssueRedactionService
    from .issue_remote_links import IssueRemoteLinksService as IssueRemoteLinksService
    from .issue_resolutions import IssueResolutionsService as IssueResolutionsService
    from .issue_search import IssueSearchService as IssueSearchService
    from .issue_security_level import IssueSecurityLevelService as IssueSecurityLevelService
    from .issue_security_schemes import IssueSecuritySchemesService as IssueSecuritySchemesService
    from .issue_type_properties import IssueTypePropertiesService as IssueTypePropertiesService
    from .issue_type_schemes import IssueTypeSchemesService as IssueTypeSchemesService
    from .issue_type_screen_schemes import IssueTypeScreenSchemesService as IssueTypeScreenSchemesService
    from .issue_types import IssueTypesService as IssueTypesService
    from .issue_votes import IssueVotesService as IssueVotesService
    from .issue_watchers import IssueWatchersService as IssueWatchersService
    from .issue_worklog_properties import IssueWorklogPropertiesService as IssueWorklogPropertiesService
    from .issue_worklogs import IssueWorklogsService as IssueWorklogsService
    from .issues import IssuesService as IssuesService
    from .jira_expressions import JiraExpressionsService as JiraExpressionsService
    from .jira_settings import JiraSettingsService as JiraSettingsService
    from .jql import JQLService as JQLService
    from .jql_functions_apps import JQLFunctionsAppsService as JQLFunctionsAppsService
    from .labels import LabelsService as LabelsService
    from .license_metrics import LicenseMetricsService as LicenseMetricsService
    from .myself import MyselfService as MyselfService
    from .permission_schemes import PermissionSchemesService as PermissionSchemesService
    from .permissions import PermissionsService as PermissionsService
    from .plans import PlansService as PlansService
    from .policies import PoliciesService as PoliciesService
    from .priority_schemes import PrioritySchemesService as PrioritySchemesService
    from .project_avatars import ProjectAvatarsService as ProjectAvatarsService
    from .project_categories import ProjectCategoriesService as ProjectCategoriesService
    from .project_classification_levels import ProjectClassificationLevelsService as ProjectClassificationLevelsService
    from .project_components import ProjectComponentsService as ProjectComponentsService
    from .project_email import ProjectEmailService as ProjectEmailService
    from .project_features import ProjectFeaturesService as ProjectFeaturesService
    from .project_key_and_name_validation import ProjectKeyAndNameValidationService as ProjectKeyAndNameValidationService
    from .project_permission_schemes import ProjectPermissionSchemesService as ProjectPermissionSchemesService
    from .project_properties import ProjectPropertiesService as ProjectPropertiesService
    from .project_role_actors import ProjectRoleActorsService as ProjectRoleActorsService
    from .project_roles import ProjectRolesService as ProjectRolesService
    from .project_templates import ProjectTemplatesService as ProjectTemplatesService
    from .project_types import ProjectTypesService as ProjectTypesService
    from .project_versions import ProjectVersionsService as ProjectVersionsService
    from .projects import ProjectsService as ProjectsService
    from .screen_schemes import ScreenSchemesService as ScreenSchemesService
    from .screen_tab_fields import ScreenTabFieldsService as ScreenTabFieldsService
    from .screen_tabs import ScreenTabsService as ScreenTabsService
    from .screens import ScreensService as ScreensService
    from .server_info import ServerInfoService as ServerInfoService
    from .service_registry import ServiceRegistryService as ServiceRegistryService
    from .status import StatusService as StatusService
    from .tasks import TasksService as TasksService
    from .teams_in_plan import TeamsInPlanService as TeamsInPlanService
    from .time_tracking import TimeTrackingService as TimeTrackingService
    from .ui_modifications_apps import UIModificationsAppsService as UIModificationsAppsService
    from .user_properties import UserPropertiesService as UserPropertiesService
    from .user_search import UserSearchService as UserSearchService
    from .users import UsersService as UsersService
    from .webhooks import WebhooksService as WebhooksService
    from .workflow_scheme_drafts import WorkflowSchemeDraftsService as WorkflowSchemeDraftsService
    from .workflow_scheme_project_associations import WorkflowSchemeProjectAssociationsService as WorkflowSchemeProjectAssociationsService
    from .workflow_schemes import WorkflowSchemesService as WorkflowSchemesService
    from .workflow_status_categories import WorkflowStatusCategoriesService as WorkflowStatusCategoriesService
    from .workflow_statuses import WorkflowStatusesService as WorkflowStatusesService
    from .workflow_transition_rules import WorkflowTransitionRulesService as WorkflowTransitionRulesService
    from .workflows import WorkflowsService as WorkflowsService

_LAZY_EXPORTS: dict[str, tuple[str, str]] = {
    "AgentsService": (".agents", "AgentsService"),
    "AnnouncementBannerService": (".announcement_banner", "AnnouncementBannerService"),
    "AppDataPoliciesService": (".app_data_policies", "AppDataPoliciesService"),
    "AppMigrationService": (".app_migration", "AppMigrationService"),
    "AppPropertiesService": (".app_properties", "AppPropertiesService"),
    "ApplicationRolesService": (".application_roles", "ApplicationRolesService"),
    "AuditRecordsService": (".audit_records", "AuditRecordsService"),
    "AvatarsService": (".avatars", "AvatarsService"),
    "ClassificationLevelsService": (".classification_levels", "ClassificationLevelsService"),
    "ConnectToForgeMigrationService": (".connect_to_forge_migration", "ConnectToForgeMigrationService"),
    "DashboardsService": (".dashboards", "DashboardsService"),
    "DynamicModulesService": (".dynamic_modules", "DynamicModulesService"),
    "FieldSchemesService": (".field_schemes", "FieldSchemesService"),
    "FilterSharingService": (".filter_sharing", "FilterSharingService"),
    "FiltersService": (".filters", "FiltersService"),
    "GroupAndUserPickerService": (".group_and_user_picker", "GroupAndUserPickerService"),
    "GroupsService": (".groups", "GroupsService"),
    "IssueAttachmentsService": (".issue_attachments", "IssueAttachmentsService"),
    "IssueBulkOperationsService": (".issue_bulk_operations", "IssueBulkOperationsService"),
    "IssueCommentPropertiesService": (".issue_comment_properties", "IssueCommentPropertiesService"),
    "IssueCommentsService": (".issue_comments", "IssueCommentsService"),
    "IssueCustomFieldAssociationsService": (".issue_custom_field_associations", "IssueCustomFieldAssociationsService"),
    "IssueCustomFieldConfigurationAppsService": (".issue_custom_field_configuration_apps", "IssueCustomFieldConfigurationAppsService"),
    "IssueCustomFieldContextsService": (".issue_custom_field_contexts", "IssueCustomFieldContextsService"),
    "IssueCustomFieldOptionsService": (".issue_custom_field_options", "IssueCustomFieldOptionsService"),
    "IssueCustomFieldOptionsAppsService": (".issue_custom_field_options_apps", "IssueCustomFieldOptionsAppsService"),
    "IssueCustomFieldValuesAppsService": (".issue_custom_field_values_apps", "IssueCustomFieldValuesAppsService"),
    "IssueFieldConfigurationsService": (".issue_field_configurations", "IssueFieldConfigurationsService"),
    "IssueFieldsService": (".issue_fields", "IssueFieldsService"),
    "IssueLinkTypesService": (".issue_link_types", "IssueLinkTypesService"),
    "IssueLinksService": (".issue_links", "IssueLinksService"),
    "IssueNavigatorSettingsService": (".issue_navigator_settings", "IssueNavigatorSettingsService"),
    "IssueNotificationSchemesService": (".issue_notification_schemes", "IssueNotificationSchemesService"),
    "IssuePanelsService": (".issue_panels", "IssuePanelsService"),
    "IssuePrioritiesService": (".issue_priorities", "IssuePrioritiesService"),
    "IssuePropertiesService": (".issue_properties", "IssuePropertiesService"),
    "IssueRedactionService": (".issue_redaction", "IssueRedactionService"),
    "IssueRemoteLinksService": (".issue_remote_links", "IssueRemoteLinksService"),
    "IssueResolutionsService": (".issue_resolutions", "IssueResolutionsService"),
    "IssueSearchService": (".issue_search", "IssueSearchService"),
    "IssueSecurityLevelService": (".issue_security_level", "IssueSecurityLevelService"),
    "IssueSecuritySchemesService": (".issue_security_schemes", "IssueSecuritySchemesService"),
    "IssueTypePropertiesService": (".issue_type_properties", "IssueTypePropertiesService"),
    "IssueTypeSchemesService": (".issue_type_schemes", "IssueTypeSchemesService"),
    "IssueTypeScreenSchemesService": (".issue_type_screen_schemes", "IssueTypeScreenSchemesService"),
    "IssueTypesService": (".issue_types", "IssueTypesService"),
    "IssueVotesService": (".issue_votes", "IssueVotesService"),
    "IssueWatchersService": (".issue_watchers", "IssueWatchersService"),
    "IssueWorklogPropertiesService": (".issue_worklog_properties", "IssueWorklogPropertiesService"),
    "IssueWorklogsService": (".issue_worklogs", "IssueWorklogsService"),
    "IssuesService": (".issues", "IssuesService"),
    "JiraExpressionsService": (".jira_expressions", "JiraExpressionsService"),
    "JiraSettingsService": (".jira_settings", "JiraSettingsService"),
    "JQLService": (".jql", "JQLService"),
    "JQLFunctionsAppsService": (".jql_functions_apps", "JQLFunctionsAppsService"),
    "LabelsService": (".labels", "LabelsService"),
    "LicenseMetricsService": (".license_metrics", "LicenseMetricsService"),
    "MyselfService": (".myself", "MyselfService"),
    "PermissionSchemesService": (".permission_schemes", "PermissionSchemesService"),
    "PermissionsService": (".permissions", "PermissionsService"),
    "PlansService": (".plans", "PlansService"),
    "PoliciesService": (".policies", "PoliciesService"),
    "PrioritySchemesService": (".priority_schemes", "PrioritySchemesService"),
    "ProjectAvatarsService": (".project_avatars", "ProjectAvatarsService"),
    "ProjectCategoriesService": (".project_categories", "ProjectCategoriesService"),
    "ProjectClassificationLevelsService": (".project_classification_levels", "ProjectClassificationLevelsService"),
    "ProjectComponentsService": (".project_components", "ProjectComponentsService"),
    "ProjectEmailService": (".project_email", "ProjectEmailService"),
    "ProjectFeaturesService": (".project_features", "ProjectFeaturesService"),
    "ProjectKeyAndNameValidationService": (".project_key_and_name_validation", "ProjectKeyAndNameValidationService"),
    "ProjectPermissionSchemesService": (".project_permission_schemes", "ProjectPermissionSchemesService"),
    "ProjectPropertiesService": (".project_properties", "ProjectPropertiesService"),
    "ProjectRoleActorsService": (".project_role_actors", "ProjectRoleActorsService"),
    "ProjectRolesService": (".project_roles", "ProjectRolesService"),
    "ProjectTemplatesService": (".project_templates", "ProjectTemplatesService"),
    "ProjectTypesService": (".project_types", "ProjectTypesService"),
    "ProjectVersionsService": (".project_versions", "ProjectVersionsService"),
    "ProjectsService": (".projects", "ProjectsService"),
    "ScreenSchemesService": (".screen_schemes", "ScreenSchemesService"),
    "ScreenTabFieldsService": (".screen_tab_fields", "ScreenTabFieldsService"),
    "ScreenTabsService": (".screen_tabs", "ScreenTabsService"),
    "ScreensService": (".screens", "ScreensService"),
    "ServerInfoService": (".server_info", "ServerInfoService"),
    "ServiceRegistryService": (".service_registry", "ServiceRegistryService"),
    "StatusService": (".status", "StatusService"),
    "TasksService": (".tasks", "TasksService"),
    "TeamsInPlanService": (".teams_in_plan", "TeamsInPlanService"),
    "TimeTrackingService": (".time_tracking", "TimeTrackingService"),
    "UIModificationsAppsService": (".ui_modifications_apps", "UIModificationsAppsService"),
    "UserPropertiesService": (".user_properties", "UserPropertiesService"),
    "UserSearchService": (".user_search", "UserSearchService"),
    "UsersService": (".users", "UsersService"),
    "WebhooksService": (".webhooks", "WebhooksService"),
    "WorkflowSchemeDraftsService": (".workflow_scheme_drafts", "WorkflowSchemeDraftsService"),
    "WorkflowSchemeProjectAssociationsService": (".workflow_scheme_project_associations", "WorkflowSchemeProjectAssociationsService"),
    "WorkflowSchemesService": (".workflow_schemes", "WorkflowSchemesService"),
    "WorkflowStatusCategoriesService": (".workflow_status_categories", "WorkflowStatusCategoriesService"),
    "WorkflowStatusesService": (".workflow_statuses", "WorkflowStatusesService"),
    "WorkflowTransitionRulesService": (".workflow_transition_rules", "WorkflowTransitionRulesService"),
    "WorkflowsService": (".workflows", "WorkflowsService"),
}

__all__ = [
    "JiraBaseService",
    *sorted(_LAZY_EXPORTS.keys()),
]


def __getattr__(name: str) -> Any:
    if name in _LAZY_EXPORTS:
        module_path, attr = _LAZY_EXPORTS[name]
        module = importlib.import_module(module_path, __name__)
        value = getattr(module, attr)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
