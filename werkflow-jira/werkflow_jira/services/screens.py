from __future__ import annotations

from typing import Any
from ..models.api import (
    PageBeanScreen,
    PageBeanScreenWithTab,
    Screen,
    ScreenDetails,
    ScreenableField,
    UpdateScreenDetails,
)
from .base import JiraBaseService


class ScreensService(JiraBaseService):
    """Jira Cloud REST API v3 — Screens (7 operations)."""

    async def add_field_to_default_screen(
        self,
        field_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/screens/addToDefault/{fieldId} — Add field to default screen"""
        response = await self._request(
            'POST',
            '/rest/api/3/screens/addToDefault/{fieldId}',
            path_params={'fieldId': field_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def create_screen(
        self,
        body: ScreenDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Screen:
        """POST /rest/api/3/screens — Create screen"""
        response = await self._request(
            'POST',
            '/rest/api/3/screens',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Screen)

    async def delete_screen(
        self,
        screen_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/screens/{screenId} — Delete screen"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/screens/{screenId}',
            path_params={'screenId': screen_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_available_screen_fields(
        self,
        screen_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ScreenableField]:
        """GET /rest/api/3/screens/{screenId}/availableFields — Get available screen fields"""
        response = await self._request(
            'GET',
            '/rest/api/3/screens/{screenId}/availableFields',
            path_params={'screenId': screen_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ScreenableField)

    async def get_screens(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id: list[int] | None = None,
        query_string: str | None = None,
        scope: list[str] | None = None,
        order_by: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanScreen:
        """GET /rest/api/3/screens — Get screens"""
        response = await self._request(
            'GET',
            '/rest/api/3/screens',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'queryString': query_string, 'scope': scope, 'orderBy': order_by},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanScreen)

    async def get_screens_for_field(
        self,
        field_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanScreenWithTab:
        """GET /rest/api/3/field/{fieldId}/screens — Get screens for a field"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldId}/screens',
            path_params={'fieldId': field_id},
            query_params={'startAt': start_at, 'maxResults': max_results, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanScreenWithTab)

    async def update_screen(
        self,
        screen_id: int,
        body: UpdateScreenDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Screen:
        """PUT /rest/api/3/screens/{screenId} — Update screen"""
        response = await self._request(
            'PUT',
            '/rest/api/3/screens/{screenId}',
            path_params={'screenId': screen_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Screen)
