from __future__ import annotations

from typing import Any
from ..models.api import (
    CreateResolutionDetails,
    PageBeanResolutionJsonBean,
    ReorderIssueResolutionsRequest,
    Resolution,
    ResolutionId,
    SetDefaultResolutionRequest,
    UpdateResolutionDetails,
)
from .base import JiraBaseService


class IssueResolutionsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue resolutions (8 operations)."""

    async def create_resolution(
        self,
        body: CreateResolutionDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ResolutionId:
        """POST /rest/api/3/resolution — Create resolution"""
        response = await self._request(
            'POST',
            '/rest/api/3/resolution',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ResolutionId)

    async def delete_resolution(
        self,
        id: str,
        replace_with: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/resolution/{id} — Delete resolution"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/resolution/{id}',
            path_params={'id': id},
            query_params={'replaceWith': replace_with},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_resolution(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Resolution:
        """GET /rest/api/3/resolution/{id} — Get resolution"""
        response = await self._request(
            'GET',
            '/rest/api/3/resolution/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Resolution)

    async def get_resolutions(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[Resolution]:
        """GET /rest/api/3/resolution — Get resolutions"""
        response = await self._request(
            'GET',
            '/rest/api/3/resolution',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, Resolution)

    async def move_resolutions(
        self,
        body: ReorderIssueResolutionsRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/resolution/move — Move resolutions"""
        response = await self._request(
            'PUT',
            '/rest/api/3/resolution/move',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def search_resolutions(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id: list[str] | None = None,
        only_default: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanResolutionJsonBean:
        """GET /rest/api/3/resolution/search — Search resolutions"""
        response = await self._request(
            'GET',
            '/rest/api/3/resolution/search',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'onlyDefault': only_default},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanResolutionJsonBean)

    async def set_default_resolution(
        self,
        body: SetDefaultResolutionRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/resolution/default — Set default resolution"""
        response = await self._request(
            'PUT',
            '/rest/api/3/resolution/default',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_resolution(
        self,
        id: str,
        body: UpdateResolutionDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/resolution/{id} — Update resolution"""
        response = await self._request(
            'PUT',
            '/rest/api/3/resolution/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
