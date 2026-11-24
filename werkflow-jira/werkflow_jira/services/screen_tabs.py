from __future__ import annotations

from typing import Any
from ..models.api import (
    ScreenableTab,
)
from .base import JiraBaseService


class ScreenTabsService(JiraBaseService):
    """Jira Cloud REST API v3 — Screen tabs (6 operations)."""

    async def add_screen_tab(
        self,
        screen_id: int,
        body: ScreenableTab | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ScreenableTab:
        """POST /rest/api/3/screens/{screenId}/tabs — Create screen tab"""
        response = await self._request(
            'POST',
            '/rest/api/3/screens/{screenId}/tabs',
            path_params={'screenId': screen_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ScreenableTab)

    async def delete_screen_tab(
        self,
        screen_id: int,
        tab_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/screens/{screenId}/tabs/{tabId} — Delete screen tab"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/screens/{screenId}/tabs/{tabId}',
            path_params={'screenId': screen_id, 'tabId': tab_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_all_screen_tabs(
        self,
        screen_id: int,
        *,
        project_key: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ScreenableTab]:
        """GET /rest/api/3/screens/{screenId}/tabs — Get all screen tabs"""
        response = await self._request(
            'GET',
            '/rest/api/3/screens/{screenId}/tabs',
            path_params={'screenId': screen_id},
            query_params={'projectKey': project_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ScreenableTab)

    async def get_bulk_screen_tabs(
        self,
        *,
        screen_id: list[int] | None = None,
        tab_id: list[int] | None = None,
        start_at: int | None = None,
        max_result: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """GET /rest/api/3/screens/tabs — Get bulk screen tabs"""
        response = await self._request(
            'GET',
            '/rest/api/3/screens/tabs',
            query_params={'screenId': screen_id, 'tabId': tab_id, 'startAt': start_at, 'maxResult': max_result},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def move_screen_tab(
        self,
        screen_id: int,
        tab_id: int,
        pos: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos} — Move screen tab"""
        response = await self._request(
            'POST',
            '/rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}',
            path_params={'screenId': screen_id, 'tabId': tab_id, 'pos': pos},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def rename_screen_tab(
        self,
        screen_id: int,
        tab_id: int,
        body: ScreenableTab | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ScreenableTab:
        """PUT /rest/api/3/screens/{screenId}/tabs/{tabId} — Update screen tab"""
        response = await self._request(
            'PUT',
            '/rest/api/3/screens/{screenId}/tabs/{tabId}',
            path_params={'screenId': screen_id, 'tabId': tab_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ScreenableTab)
