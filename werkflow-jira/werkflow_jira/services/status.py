from __future__ import annotations

from typing import Any
from ..models.api import (
    JiraStatus,
    PageOfStatuses,
    StatusCreateRequest,
    StatusProjectIssueTypeUsageDTO,
    StatusProjectUsageDTO,
    StatusUpdateRequest,
    StatusWorkflowUsageDTO,
)
from .base import JiraBaseService


class StatusService(JiraBaseService):
    """Jira Cloud REST API v3 — Status (9 operations)."""

    async def create_statuses(
        self,
        body: StatusCreateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[JiraStatus]:
        """POST /rest/api/3/statuses — Bulk create statuses"""
        response = await self._request(
            'POST',
            '/rest/api/3/statuses',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, JiraStatus)

    async def delete_statuses_by_id(
        self,
        id: list[str],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/statuses — Bulk delete Statuses"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/statuses',
            query_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_project_issue_type_usages_for_status(
        self,
        status_id: str,
        project_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> StatusProjectIssueTypeUsageDTO:
        """GET /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages — Get issue type usages by status and project"""
        response = await self._request(
            'GET',
            '/rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages',
            path_params={'statusId': status_id, 'projectId': project_id},
            query_params={'nextPageToken': next_page_token, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, StatusProjectIssueTypeUsageDTO)

    async def get_project_usages_for_status(
        self,
        status_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> StatusProjectUsageDTO:
        """GET /rest/api/3/statuses/{statusId}/projectUsages — Get project usages by status"""
        response = await self._request(
            'GET',
            '/rest/api/3/statuses/{statusId}/projectUsages',
            path_params={'statusId': status_id},
            query_params={'nextPageToken': next_page_token, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, StatusProjectUsageDTO)

    async def get_statuses_by_id(
        self,
        id: list[str],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[JiraStatus]:
        """GET /rest/api/3/statuses — Bulk get statuses"""
        response = await self._request(
            'GET',
            '/rest/api/3/statuses',
            query_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, JiraStatus)

    async def get_statuses_by_name(
        self,
        name: list[str],
        *,
        project_id: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[JiraStatus]:
        """GET /rest/api/3/statuses/byNames — Bulk get statuses by name"""
        response = await self._request(
            'GET',
            '/rest/api/3/statuses/byNames',
            query_params={'name': name, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, JiraStatus)

    async def get_workflow_usages_for_status(
        self,
        status_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> StatusWorkflowUsageDTO:
        """GET /rest/api/3/statuses/{statusId}/workflowUsages — Get workflow usages by status"""
        response = await self._request(
            'GET',
            '/rest/api/3/statuses/{statusId}/workflowUsages',
            path_params={'statusId': status_id},
            query_params={'nextPageToken': next_page_token, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, StatusWorkflowUsageDTO)

    async def search(
        self,
        *,
        project_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        search_string: str | None = None,
        status_category: str | None = None,
        include_global_statuses: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageOfStatuses:
        """GET /rest/api/3/statuses/search — Search statuses paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/statuses/search',
            query_params={'projectId': project_id, 'startAt': start_at, 'maxResults': max_results, 'searchString': search_string, 'statusCategory': status_category, 'includeGlobalStatuses': include_global_statuses},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageOfStatuses)

    async def update_statuses(
        self,
        body: StatusUpdateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/statuses — Bulk update statuses"""
        response = await self._request(
            'PUT',
            '/rest/api/3/statuses',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
