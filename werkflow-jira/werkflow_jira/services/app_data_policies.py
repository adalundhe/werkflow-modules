from __future__ import annotations

from ..models.api import (
    ProjectDataPolicies,
    WorkspaceDataPolicy,
)
from .base import JiraBaseService


class AppDataPoliciesService(JiraBaseService):
    """Jira Cloud REST API v3 — App data policies (2 operations)."""

    async def get_policies(
        self,
        *,
        ids: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectDataPolicies:
        """GET /rest/api/3/data-policy/project — Get data policy for projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/data-policy/project',
            query_params={'ids': ids},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectDataPolicies)

    async def get_policy(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkspaceDataPolicy:
        """GET /rest/api/3/data-policy — Get data policy for the workspace"""
        response = await self._request(
            'GET',
            '/rest/api/3/data-policy',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkspaceDataPolicy)
