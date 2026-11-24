from __future__ import annotations

from typing import Any
from ..models.api import (
    CreatePriorityDetails,
    PageBeanPriority,
    Priority,
    PriorityId,
    ReorderIssuePriorities,
    SetDefaultPriorityRequest,
    UpdatePriorityDetails,
)
from .base import JiraBaseService


class IssuePrioritiesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue priorities (8 operations)."""

    async def create_priority(
        self,
        body: CreatePriorityDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PriorityId:
        """POST /rest/api/3/priority — Create priority"""
        response = await self._request(
            'POST',
            '/rest/api/3/priority',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PriorityId)

    async def delete_priority(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/priority/{id} — Delete priority"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/priority/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_priorities(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[Priority]:
        """GET /rest/api/3/priority — Get priorities"""
        response = await self._request(
            'GET',
            '/rest/api/3/priority',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, Priority)

    async def get_priority(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Priority:
        """GET /rest/api/3/priority/{id} — Get priority"""
        response = await self._request(
            'GET',
            '/rest/api/3/priority/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Priority)

    async def move_priorities(
        self,
        body: ReorderIssuePriorities | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/priority/move — Move priorities"""
        response = await self._request(
            'PUT',
            '/rest/api/3/priority/move',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def search_priorities(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id: list[str] | None = None,
        project_id: list[str] | None = None,
        priority_name: str | None = None,
        only_default: bool | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanPriority:
        """GET /rest/api/3/priority/search — Search priorities"""
        response = await self._request(
            'GET',
            '/rest/api/3/priority/search',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'projectId': project_id, 'priorityName': priority_name, 'onlyDefault': only_default, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanPriority)

    async def set_default_priority(
        self,
        body: SetDefaultPriorityRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/priority/default — Set default priority"""
        response = await self._request(
            'PUT',
            '/rest/api/3/priority/default',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_priority(
        self,
        id: str,
        body: UpdatePriorityDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/priority/{id} — Update priority"""
        response = await self._request(
            'PUT',
            '/rest/api/3/priority/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
