from __future__ import annotations

from typing import Any
from ..models.api import (
    AddFieldBean,
    MoveFieldBean,
    ScreenableField,
)
from .base import JiraBaseService


class ScreenTabFieldsService(JiraBaseService):
    """Jira Cloud REST API v3 — Screen tab fields (4 operations)."""

    async def add_screen_tab_field(
        self,
        screen_id: int,
        tab_id: int,
        body: AddFieldBean | dict[str, Any],
        *,
        skip_field_association: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ScreenableField:
        """POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields — Add screen tab field"""
        response = await self._request(
            'POST',
            '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields',
            path_params={'screenId': screen_id, 'tabId': tab_id},
            query_params={'skipFieldAssociation': skip_field_association},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ScreenableField)

    async def get_all_screen_tab_fields(
        self,
        screen_id: int,
        tab_id: int,
        *,
        project_key: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ScreenableField]:
        """GET /rest/api/3/screens/{screenId}/tabs/{tabId}/fields — Get all screen tab fields"""
        response = await self._request(
            'GET',
            '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields',
            path_params={'screenId': screen_id, 'tabId': tab_id},
            query_params={'projectKey': project_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ScreenableField)

    async def move_screen_tab_field(
        self,
        screen_id: int,
        tab_id: int,
        id: str,
        body: MoveFieldBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move — Move screen tab field"""
        response = await self._request(
            'POST',
            '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move',
            path_params={'screenId': screen_id, 'tabId': tab_id, 'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def remove_screen_tab_field(
        self,
        screen_id: int,
        tab_id: int,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id} — Remove screen tab field"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}',
            path_params={'screenId': screen_id, 'tabId': tab_id, 'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None
