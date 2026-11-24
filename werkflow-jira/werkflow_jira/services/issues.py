from __future__ import annotations

from typing import Any
from ..models.api import (
    ArchiveIssueAsyncRequest,
    ArchivedIssuesFilterRequest,
    BulkChangelogRequestBean,
    BulkChangelogResponseBean,
    BulkFetchIssueRequestBean,
    BulkIssueResults,
    CreatedIssue,
    CreatedIssues,
    ExportArchivedIssuesTaskProgressResponse,
    IssueArchivalSyncRequest,
    IssueArchivalSyncResponse,
    IssueBean,
    IssueChangelogIds,
    IssueCreateMetadata,
    IssueEvent,
    IssueLimitReportResponseBean,
    IssueUpdateDetails,
    IssueUpdateMetadata,
    IssuesUpdateBean,
    Notification,
    PageBeanChangelog,
    PageOfChangelogs,
    PageOfCreateMetaIssueTypeWithField,
    PageOfCreateMetaIssueTypes,
    Transitions,
    User,
)
from .base import JiraBaseService


class IssuesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issues (24 operations)."""

    async def archive_issues(
        self,
        body: IssueArchivalSyncRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueArchivalSyncResponse:
        """PUT /rest/api/3/issue/archive — Archive issue(s) by issue ID/key"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issue/archive',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueArchivalSyncResponse)

    async def archive_issues_async(
        self,
        body: ArchiveIssueAsyncRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> str:
        """POST /rest/api/3/issue/archive — Archive issue(s) by JQL"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/archive',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        payload = self._parse_json(response)
        return str(payload) if payload is not None else ""

    async def assign_issue(
        self,
        issue_id_or_key: str,
        body: User | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issue/{issueIdOrKey}/assignee — Assign issue"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issue/{issueIdOrKey}/assignee',
            path_params={'issueIdOrKey': issue_id_or_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def bulk_fetch_issues(
        self,
        body: BulkFetchIssueRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkIssueResults:
        """POST /rest/api/3/issue/bulkfetch — Bulk fetch issues"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/bulkfetch',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkIssueResults)

    async def create_issue(
        self,
        body: IssueUpdateDetails | dict[str, Any],
        *,
        update_history: bool | None = None,
        prefer_field_associated_errors: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> CreatedIssue:
        """POST /rest/api/3/issue — Create issue"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue',
            query_params={'updateHistory': update_history, 'preferFieldAssociatedErrors': prefer_field_associated_errors},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, CreatedIssue)

    async def create_issues(
        self,
        body: IssuesUpdateBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> CreatedIssues:
        """POST /rest/api/3/issue/bulk — Bulk create issue"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/bulk',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, CreatedIssues)

    async def delete_issue(
        self,
        issue_id_or_key: str,
        *,
        delete_subtasks: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/{issueIdOrKey} — Delete issue"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/{issueIdOrKey}',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'deleteSubtasks': delete_subtasks},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def do_transition(
        self,
        issue_id_or_key: str,
        body: IssueUpdateDetails | dict[str, Any],
        *,
        prefer_field_associated_errors: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/issue/{issueIdOrKey}/transitions — Transition issue"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/{issueIdOrKey}/transitions',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'preferFieldAssociatedErrors': prefer_field_associated_errors},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def edit_issue(
        self,
        issue_id_or_key: str,
        body: IssueUpdateDetails | dict[str, Any],
        *,
        notify_users: bool | None = None,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
        return_issue: bool | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issue/{issueIdOrKey} — Edit issue"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issue/{issueIdOrKey}',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'notifyUsers': notify_users, 'overrideScreenSecurity': override_screen_security, 'overrideEditableFlag': override_editable_flag, 'returnIssue': return_issue, 'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def export_archived_issues(
        self,
        body: ArchivedIssuesFilterRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ExportArchivedIssuesTaskProgressResponse:
        """PUT /rest/api/3/issues/archive/export — Export archived issue(s)"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issues/archive/export',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ExportArchivedIssuesTaskProgressResponse)

    async def get_bulk_changelogs(
        self,
        body: BulkChangelogRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkChangelogResponseBean:
        """POST /rest/api/3/changelog/bulkfetch — Bulk fetch changelogs"""
        response = await self._request(
            'POST',
            '/rest/api/3/changelog/bulkfetch',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkChangelogResponseBean)

    async def get_change_logs(
        self,
        issue_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanChangelog:
        """GET /rest/api/3/issue/{issueIdOrKey}/changelog — Get changelogs"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/changelog',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanChangelog)

    async def get_change_logs_by_ids(
        self,
        issue_id_or_key: str,
        body: IssueChangelogIds | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageOfChangelogs:
        """POST /rest/api/3/issue/{issueIdOrKey}/changelog/list — Get changelogs by IDs"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/{issueIdOrKey}/changelog/list',
            path_params={'issueIdOrKey': issue_id_or_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageOfChangelogs)

    async def get_create_issue_meta(
        self,
        *,
        project_ids: list[str] | None = None,
        project_keys: list[str] | None = None,
        issuetype_ids: list[str] | None = None,
        issuetype_names: list[str] | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueCreateMetadata:
        """GET /rest/api/3/issue/createmeta — Get create issue metadata"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/createmeta',
            query_params={'projectIds': project_ids, 'projectKeys': project_keys, 'issuetypeIds': issuetype_ids, 'issuetypeNames': issuetype_names, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueCreateMetadata)

    async def get_create_issue_meta_issue_type_id(
        self,
        project_id_or_key: str,
        issue_type_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageOfCreateMetaIssueTypeWithField:
        """GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId} — Get create field metadata for a project and issue type id"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}',
            path_params={'projectIdOrKey': project_id_or_key, 'issueTypeId': issue_type_id},
            query_params={'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageOfCreateMetaIssueTypeWithField)

    async def get_create_issue_meta_issue_types(
        self,
        project_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageOfCreateMetaIssueTypes:
        """GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes — Get create metadata issue types for a project"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageOfCreateMetaIssueTypes)

    async def get_edit_issue_meta(
        self,
        issue_id_or_key: str,
        *,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueUpdateMetadata:
        """GET /rest/api/3/issue/{issueIdOrKey}/editmeta — Get edit issue metadata"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/editmeta',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'overrideScreenSecurity': override_screen_security, 'overrideEditableFlag': override_editable_flag},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueUpdateMetadata)

    async def get_events(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[IssueEvent]:
        """GET /rest/api/3/events — Get events"""
        response = await self._request(
            'GET',
            '/rest/api/3/events',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, IssueEvent)

    async def get_issue(
        self,
        issue_id_or_key: str,
        *,
        fields: list[str] | None = None,
        fields_by_keys: bool | None = None,
        expand: str | None = None,
        properties: list[str] | None = None,
        update_history: bool | None = None,
        fail_fast: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueBean:
        """GET /rest/api/3/issue/{issueIdOrKey} — Get issue"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'fields': fields, 'fieldsByKeys': fields_by_keys, 'expand': expand, 'properties': properties, 'updateHistory': update_history, 'failFast': fail_fast},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueBean)

    async def get_issue_adf_limit_report(
        self,
        *,
        is_returning_keys: bool | None = None,
        field_type: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueLimitReportResponseBean:
        """GET /rest/api/3/issue/limit/adf/report — Get issue adf limit report"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/limit/adf/report',
            query_params={'isReturningKeys': is_returning_keys, 'fieldType': field_type},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueLimitReportResponseBean)

    async def get_issue_limit_report(
        self,
        *,
        is_returning_keys: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueLimitReportResponseBean:
        """GET /rest/api/3/issue/limit/report — Get issue limit report"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/limit/report',
            query_params={'isReturningKeys': is_returning_keys},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueLimitReportResponseBean)

    async def get_transitions(
        self,
        issue_id_or_key: str,
        *,
        expand: str | None = None,
        transition_id: str | None = None,
        skip_remote_only_condition: bool | None = None,
        include_unavailable_transitions: bool | None = None,
        sort_by_ops_bar_and_status: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Transitions:
        """GET /rest/api/3/issue/{issueIdOrKey}/transitions — Get transitions"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/transitions',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'expand': expand, 'transitionId': transition_id, 'skipRemoteOnlyCondition': skip_remote_only_condition, 'includeUnavailableTransitions': include_unavailable_transitions, 'sortByOpsBarAndStatus': sort_by_ops_bar_and_status},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Transitions)

    async def notify(
        self,
        issue_id_or_key: str,
        body: Notification | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/issue/{issueIdOrKey}/notify — Send notification for issue"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/{issueIdOrKey}/notify',
            path_params={'issueIdOrKey': issue_id_or_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def unarchive_issues(
        self,
        body: IssueArchivalSyncRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueArchivalSyncResponse:
        """PUT /rest/api/3/issue/unarchive — Unarchive issue(s) by issue keys/ID"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issue/unarchive',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueArchivalSyncResponse)
