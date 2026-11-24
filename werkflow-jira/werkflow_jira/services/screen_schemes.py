from __future__ import annotations

from typing import Any
from ..models.api import (
    PageBeanScreenScheme,
    ScreenSchemeDetails,
    ScreenSchemeId,
    UpdateScreenSchemeDetails,
)
from .base import JiraBaseService


class ScreenSchemesService(JiraBaseService):
    """Jira Cloud REST API v3 — Screen schemes (4 operations)."""

    async def create_screen_scheme(
        self,
        body: ScreenSchemeDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ScreenSchemeId:
        """POST /rest/api/3/screenscheme — Create screen scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/screenscheme',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ScreenSchemeId)

    async def delete_screen_scheme(
        self,
        screen_scheme_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/screenscheme/{screenSchemeId} — Delete screen scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/screenscheme/{screenSchemeId}',
            path_params={'screenSchemeId': screen_scheme_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_screen_schemes(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id: list[int] | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanScreenScheme:
        """GET /rest/api/3/screenscheme — Get screen schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/screenscheme',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'expand': expand, 'queryString': query_string, 'orderBy': order_by},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanScreenScheme)

    async def update_screen_scheme(
        self,
        screen_scheme_id: str,
        body: UpdateScreenSchemeDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/screenscheme/{screenSchemeId} — Update screen scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/screenscheme/{screenSchemeId}',
            path_params={'screenSchemeId': screen_scheme_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
