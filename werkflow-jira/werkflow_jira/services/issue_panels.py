from __future__ import annotations

from typing import Any
from ..models.api import (
    ForgePanelProjectPinAsyncResponse,
    ForgePanelProjectPinRequest,
    ForgePanelProjectPinStatusRequest,
    ForgePanelProjectPinStatusResponse,
)
from .base import JiraBaseService


class IssuePanelsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue panels (2 operations)."""

    async def bulk_pin_unpin_projects_async(
        self,
        body: ForgePanelProjectPinRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ForgePanelProjectPinAsyncResponse:
        """POST /rest/api/3/forge/panel/action/bulk/async — Bulk pin or unpin issue panel to projects"""
        response = await self._request(
            'POST',
            '/rest/api/3/forge/panel/action/bulk/async',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ForgePanelProjectPinAsyncResponse)

    async def get_bulk_pin_status(
        self,
        body: ForgePanelProjectPinStatusRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ForgePanelProjectPinStatusResponse:
        """POST /rest/api/3/forge/panel/action/bulk/status — Get issue panel pin status for projects"""
        response = await self._request(
            'POST',
            '/rest/api/3/forge/panel/action/bulk/status',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ForgePanelProjectPinStatusResponse)
