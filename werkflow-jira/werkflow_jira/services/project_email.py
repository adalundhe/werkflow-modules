from __future__ import annotations

from typing import Any
from ..models.api import (
    ProjectEmailAddress,
)
from .base import JiraBaseService


class ProjectEmailService(JiraBaseService):
    """Jira Cloud REST API v3 — Project email (2 operations)."""

    async def get_project_email(
        self,
        project_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectEmailAddress:
        """GET /rest/api/3/project/{projectId}/email — Get project's sender email"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectId}/email',
            path_params={'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectEmailAddress)

    async def update_project_email(
        self,
        project_id: int,
        body: ProjectEmailAddress | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/project/{projectId}/email — Set project's sender email"""
        response = await self._request(
            'PUT',
            '/rest/api/3/project/{projectId}/email',
            path_params={'projectId': project_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
