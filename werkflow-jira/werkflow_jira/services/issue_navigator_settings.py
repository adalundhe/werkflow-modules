from __future__ import annotations

from typing import Any
from ..models.api import (
    ColumnItem,
    ColumnRequestBody,
)
from .base import JiraBaseService


class IssueNavigatorSettingsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue navigator settings (2 operations)."""

    async def get_issue_navigator_default_columns(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ColumnItem]:
        """GET /rest/api/3/settings/columns — Get issue navigator default columns"""
        response = await self._request(
            'GET',
            '/rest/api/3/settings/columns',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ColumnItem)

    async def set_issue_navigator_default_columns(
        self,
        body: ColumnRequestBody | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """PUT /rest/api/3/settings/columns — Set issue navigator default columns"""
        response = await self._request(
            'PUT',
            '/rest/api/3/settings/columns',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None
