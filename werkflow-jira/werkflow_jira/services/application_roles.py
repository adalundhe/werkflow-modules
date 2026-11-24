from __future__ import annotations

from ..models.api import (
    ApplicationRole,
)
from .base import JiraBaseService


class ApplicationRolesService(JiraBaseService):
    """Jira Cloud REST API v3 — Application roles (2 operations)."""

    async def get_all_application_roles(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ApplicationRole]:
        """GET /rest/api/3/applicationrole — Get all application roles"""
        response = await self._request(
            'GET',
            '/rest/api/3/applicationrole',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ApplicationRole)

    async def get_application_role(
        self,
        key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ApplicationRole:
        """GET /rest/api/3/applicationrole/{key} — Get application role"""
        response = await self._request(
            'GET',
            '/rest/api/3/applicationrole/{key}',
            path_params={'key': key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ApplicationRole)
