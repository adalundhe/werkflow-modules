from __future__ import annotations

from ..models.api import (
    ServerInformation,
)
from .base import JiraBaseService


class ServerInfoService(JiraBaseService):
    """Jira Cloud REST API v3 — Server info (1 operations)."""

    async def get_server_info(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ServerInformation:
        """GET /rest/api/3/serverInfo — Get Jira instance info"""
        response = await self._request(
            'GET',
            '/rest/api/3/serverInfo',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ServerInformation)
