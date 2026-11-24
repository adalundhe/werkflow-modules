from __future__ import annotations

from ..models.api import (
    StatusDetails,
)
from .base import JiraBaseService


class WorkflowStatusesService(JiraBaseService):
    """Jira Cloud REST API v3 — Workflow statuses (2 operations)."""

    async def get_status(
        self,
        id_or_name: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> StatusDetails:
        """GET /rest/api/3/status/{idOrName} — Get status"""
        response = await self._request(
            'GET',
            '/rest/api/3/status/{idOrName}',
            path_params={'idOrName': id_or_name},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, StatusDetails)

    async def get_statuses(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[StatusDetails]:
        """GET /rest/api/3/status — Get all statuses"""
        response = await self._request(
            'GET',
            '/rest/api/3/status',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, StatusDetails)
