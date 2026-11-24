# werkflow-jira

Version `0.5.0`

Strictly-typed asynchronous **Jira Cloud REST API v3** client for [Werkflow](https://github.com/adalundhe/werkflow), providing full OpenAPI v3 coverage across **100 resource services (630 endpoints)**, 1,002 Pydantic v2 one-model-per-file API schemas, typed Atlassian Document Format (ADF) content builders, and high-level issue convenience helpers.

## Installation

```bash
pip install werkflow-jira
```

## Features

- **Complete Jira Cloud REST API v3 Coverage:** 100 lazily-loaded typed async service classes covering all 630 endpoints from Atlassian's official OpenAPI 3.0.1 specification (`swagger-v3.v3.json`).
- **One-Model-Per-File Pydantic v2 Schemas:** 1,002 strictly-typed models and union/list aliases under `werkflow_jira.models.api`, handling OpenAPI `allOf`/`oneOf`/`anyOf`, aliased fields (such as `schema_` / `from_` / `global_` / `size_16x16`), and dynamic custom fields.
- **Flexible Authentication:** Configure default credentials once via `jira.configure(organization=..., email=..., api_token=...)` (or pass them to `Jira(...)`) and optionally override per call with `jira_organization`, `jira_email`, and `jira_api_token`.
- **Special Media Types & Uploads:** Supports JSON, `application/json-patch+json`, `text/plain`, multipart file attachments (`X-Atlassian-Token: no-check`), binary avatar uploads/downloads, and `DELETE` requests with JSON bodies.
- **Typed ADF Content Builders & Convenience Helpers:** Full backwards compatibility with `create_issue()`, `create_issue_batch()`, `get_issue()`, `create_issue_link()`, `get_jira_project()`, `list_priorities()`, and ADF models (`JiraTopLevelBlock`, `JiraChildBlock`, `JiraInlineBlock`, etc.).
- **Typed Error Handling:** Maps HTTP status codes to `BadRequestError`, `UnauthorizedRequestError`, `ResourceNotFoundError`, `MethodNotAllowedError`, `UnprocessableContentError`, and `ServerFailedError`.

## Usage

```python
from werkflow_jira import Jira
from werkflow_jira.models.api import IssueUpdateDetails

async with Jira() as jira:
    jira.configure(
        organization="my-org",
        email="bot@example.com",
        api_token="jira-api-token",
    )

    # Search issues with JQL enhanced search
    results = await jira.issue_search.search_and_reconsile_issues_using_jql(
        jql="project = ENG AND status != Done",
        fields=["summary", "status", "assignee"],
    )

    # Create a new issue using typed Pydantic models
    created = await jira.issues.create_issue(
        IssueUpdateDetails(
            fields={
                "project": {"key": "ENG"},
                "issuetype": {"name": "Task"},
                "summary": "Automate release checklist",
            }
        )
    )

    # Upload an attachment
    attachments = await jira.issue_attachments.add_attachment(
        created.key or "ENG-1",
        files=["./release-notes.md"],
    )
```

## Supported Jira Cloud REST API v3 Services (100 Services — 630 Endpoints)

| Service Attribute | Service Class | Jira API Resource Group | Endpoints |
| --- | --- | --- | ---: |
| `jira.agents` | `AgentsService` | Agents | 2 |
| `jira.announcement_banner` | `AnnouncementBannerService` | Announcement banner | 2 |
| `jira.app_data_policies` | `AppDataPoliciesService` | App data policies | 2 |
| `jira.app_migration` | `AppMigrationService` | App migration | 3 |
| `jira.app_properties` | `AppPropertiesService` | App properties | 8 |
| `jira.application_roles` | `ApplicationRolesService` | Application roles | 2 |
| `jira.audit_records` | `AuditRecordsService` | Audit records | 1 |
| `jira.avatars` | `AvatarsService` | Avatars | 7 |
| `jira.classification_levels` | `ClassificationLevelsService` | Classification levels | 1 |
| `jira.connect_to_forge_migration` | `ConnectToForgeMigrationService` | Migration of Connect modules to Forge | 2 |
| `jira.dashboards` | `DashboardsService` | Dashboards | 17 |
| `jira.dynamic_modules` | `DynamicModulesService` | Dynamic modules | 3 |
| `jira.field_schemes` | `FieldSchemesService` | Field schemes | 15 |
| `jira.filter_sharing` | `FilterSharingService` | Filter sharing | 6 |
| `jira.filters` | `FiltersService` | Filters | 13 |
| `jira.group_and_user_picker` | `GroupAndUserPickerService` | Group and user picker | 1 |
| `jira.groups` | `GroupsService` | Groups | 8 |
| `jira.issue_attachments` | `IssueAttachmentsService` | Issue attachments | 8 |
| `jira.issue_bulk_operations` | `IssueBulkOperationsService` | Issue bulk operations | 9 |
| `jira.issue_comment_properties` | `IssueCommentPropertiesService` | Issue comment properties | 4 |
| `jira.issue_comments` | `IssueCommentsService` | Issue comments | 6 |
| `jira.issue_custom_field_associations` | `IssueCustomFieldAssociationsService` | Issue custom field associations | 2 |
| `jira.issue_custom_field_configuration_apps` | `IssueCustomFieldConfigurationAppsService` | Issue custom field configuration (apps) | 3 |
| `jira.issue_custom_field_contexts` | `IssueCustomFieldContextsService` | Issue custom field contexts | 15 |
| `jira.issue_custom_field_options` | `IssueCustomFieldOptionsService` | Issue custom field options | 7 |
| `jira.issue_custom_field_options_apps` | `IssueCustomFieldOptionsAppsService` | Issue custom field options (apps) | 8 |
| `jira.issue_custom_field_values_apps` | `IssueCustomFieldValuesAppsService` | Issue custom field values (apps) | 2 |
| `jira.issue_field_configurations` | `IssueFieldConfigurationsService` | Issue field configurations | 15 |
| `jira.issue_fields` | `IssueFieldsService` | Issue fields | 11 |
| `jira.issue_link_types` | `IssueLinkTypesService` | Issue link types | 5 |
| `jira.issue_links` | `IssueLinksService` | Issue links | 3 |
| `jira.issue_navigator_settings` | `IssueNavigatorSettingsService` | Issue navigator settings | 2 |
| `jira.issue_notification_schemes` | `IssueNotificationSchemesService` | Issue notification schemes | 8 |
| `jira.issue_panels` | `IssuePanelsService` | Issue panels | 2 |
| `jira.issue_priorities` | `IssuePrioritiesService` | Issue priorities | 8 |
| `jira.issue_properties` | `IssuePropertiesService` | Issue properties | 8 |
| `jira.issue_redaction` | `IssueRedactionService` | Issue redaction | 2 |
| `jira.issue_remote_links` | `IssueRemoteLinksService` | Issue remote links | 6 |
| `jira.issue_resolutions` | `IssueResolutionsService` | Issue resolutions | 8 |
| `jira.issue_search` | `IssueSearchService` | Issue search | 7 |
| `jira.issue_security_level` | `IssueSecurityLevelService` | Issue security level | 2 |
| `jira.issue_security_schemes` | `IssueSecuritySchemesService` | Issue security schemes | 16 |
| `jira.issue_type_properties` | `IssueTypePropertiesService` | Issue type properties | 4 |
| `jira.issue_type_schemes` | `IssueTypeSchemesService` | Issue type schemes | 10 |
| `jira.issue_type_screen_schemes` | `IssueTypeScreenSchemesService` | Issue type screen schemes | 11 |
| `jira.issue_types` | `IssueTypesService` | Issue types | 8 |
| `jira.issue_votes` | `IssueVotesService` | Issue votes | 3 |
| `jira.issue_watchers` | `IssueWatchersService` | Issue watchers | 4 |
| `jira.issue_worklog_properties` | `IssueWorklogPropertiesService` | Issue worklog properties | 4 |
| `jira.issue_worklogs` | `IssueWorklogsService` | Issue worklogs | 11 |
| `jira.issues` | `IssuesService` | Issues | 24 |
| `jira.jira_expressions` | `JiraExpressionsService` | Jira expressions | 3 |
| `jira.jira_settings` | `JiraSettingsService` | Jira settings | 4 |
| `jira.jql` | `JQLService` | JQL | 7 |
| `jira.jql_functions_apps` | `JQLFunctionsAppsService` | JQL functions (apps) | 3 |
| `jira.labels` | `LabelsService` | Labels | 1 |
| `jira.license_metrics` | `LicenseMetricsService` | License metrics | 3 |
| `jira.myself` | `MyselfService` | Myself | 6 |
| `jira.permission_schemes` | `PermissionSchemesService` | Permission schemes | 9 |
| `jira.permissions` | `PermissionsService` | Permissions | 4 |
| `jira.plans` | `PlansService` | Plans | 7 |
| `jira.policies` | `PoliciesService` | Policies | 7 |
| `jira.priority_schemes` | `PrioritySchemesService` | Priority schemes | 8 |
| `jira.project_avatars` | `ProjectAvatarsService` | Project avatars | 4 |
| `jira.project_categories` | `ProjectCategoriesService` | Project categories | 5 |
| `jira.project_classification_levels` | `ProjectClassificationLevelsService` | Project classification levels | 4 |
| `jira.project_components` | `ProjectComponentsService` | Project components | 8 |
| `jira.project_email` | `ProjectEmailService` | Project email | 2 |
| `jira.project_features` | `ProjectFeaturesService` | Project features | 2 |
| `jira.project_key_and_name_validation` | `ProjectKeyAndNameValidationService` | Project key and name validation | 3 |
| `jira.project_permission_schemes` | `ProjectPermissionSchemesService` | Project permission schemes | 4 |
| `jira.project_properties` | `ProjectPropertiesService` | Project properties | 4 |
| `jira.project_role_actors` | `ProjectRoleActorsService` | Project role actors | 6 |
| `jira.project_roles` | `ProjectRolesService` | Project roles | 9 |
| `jira.project_templates` | `ProjectTemplatesService` | Project templates | 5 |
| `jira.project_types` | `ProjectTypesService` | Project types | 4 |
| `jira.project_versions` | `ProjectVersionsService` | Project versions | 15 |
| `jira.projects` | `ProjectsService` | Projects | 13 |
| `jira.screen_schemes` | `ScreenSchemesService` | Screen schemes | 4 |
| `jira.screen_tab_fields` | `ScreenTabFieldsService` | Screen tab fields | 4 |
| `jira.screen_tabs` | `ScreenTabsService` | Screen tabs | 6 |
| `jira.screens` | `ScreensService` | Screens | 7 |
| `jira.server_info` | `ServerInfoService` | Server info | 1 |
| `jira.service_registry` | `ServiceRegistryService` | Service Registry | 1 |
| `jira.status` | `StatusService` | Status | 9 |
| `jira.tasks` | `TasksService` | Tasks | 2 |
| `jira.teams_in_plan` | `TeamsInPlanService` | Teams in plan | 9 |
| `jira.time_tracking` | `TimeTrackingService` | Time tracking | 5 |
| `jira.ui_modifications_apps` | `UIModificationsAppsService` | UI modifications (apps) | 4 |
| `jira.user_properties` | `UserPropertiesService` | User properties | 4 |
| `jira.user_search` | `UserSearchService` | User search | 8 |
| `jira.users` | `UsersService` | Users | 13 |
| `jira.webhooks` | `WebhooksService` | Webhooks | 5 |
| `jira.workflow_scheme_drafts` | `WorkflowSchemeDraftsService` | Workflow scheme drafts | 14 |
| `jira.workflow_scheme_project_associations` | `WorkflowSchemeProjectAssociationsService` | Workflow scheme project associations | 2 |
| `jira.workflow_schemes` | `WorkflowSchemesService` | Workflow schemes | 19 |
| `jira.workflow_status_categories` | `WorkflowStatusCategoriesService` | Workflow status categories | 2 |
| `jira.workflow_statuses` | `WorkflowStatusesService` | Workflow statuses | 2 |
| `jira.workflow_transition_rules` | `WorkflowTransitionRulesService` | Workflow transition rules | 3 |
| `jira.workflows` | `WorkflowsService` | Workflows | 17 |

## Dependencies

- `werkflow-core`
- `werkflow-http`
- `pydantic`

## Requirements

- Python `>=3.11`
