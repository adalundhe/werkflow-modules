from __future__ import annotations

from typing import Any
from ..models.api import (
    CreateUiModificationDetails,
    PageBeanUiModificationDetails,
    UiModificationIdentifiers,
    UpdateUiModificationDetails,
)
from .base import JiraBaseService


class UIModificationsAppsService(JiraBaseService):
    """Jira Cloud REST API v3 — UI modifications (apps) (4 operations)."""

    async def create_ui_modification(
        self,
        body: CreateUiModificationDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> UiModificationIdentifiers:
        """POST /rest/api/3/uiModifications — Create UI modification"""
        response = await self._request(
            'POST',
            '/rest/api/3/uiModifications',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, UiModificationIdentifiers)

    async def delete_ui_modification(
        self,
        ui_modification_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/uiModifications/{uiModificationId} — Delete UI modification"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/uiModifications/{uiModificationId}',
            path_params={'uiModificationId': ui_modification_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_ui_modifications(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanUiModificationDetails:
        """GET /rest/api/3/uiModifications — Get UI modifications"""
        response = await self._request(
            'GET',
            '/rest/api/3/uiModifications',
            query_params={'startAt': start_at, 'maxResults': max_results, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanUiModificationDetails)

    async def update_ui_modification(
        self,
        ui_modification_id: str,
        body: UpdateUiModificationDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/uiModifications/{uiModificationId} — Update UI modification"""
        response = await self._request(
            'PUT',
            '/rest/api/3/uiModifications/{uiModificationId}',
            path_params={'uiModificationId': ui_modification_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
