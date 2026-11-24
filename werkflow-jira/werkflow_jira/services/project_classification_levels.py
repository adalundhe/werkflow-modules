from __future__ import annotations

from typing import Any
from ..models.api import (
    UpdateDefaultProjectClassificationBean,
)
from .base import JiraBaseService


class ProjectClassificationLevelsService(JiraBaseService):
    """Jira Cloud REST API v3 — Project classification levels (4 operations)."""

    async def get_default_project_classification(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """GET /rest/api/3/project/{projectIdOrKey}/classification-level/default — Get the default data classification level of a project"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/classification-level/default',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_project_classification_config(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """GET /rest/api/3/project/{projectIdOrKey}/classification-config — Get the classification configuration for a project"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/classification-config',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def remove_default_project_classification(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/project/{projectIdOrKey}/classification-level/default — Remove the default data classification level from a project"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/project/{projectIdOrKey}/classification-level/default',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_default_project_classification(
        self,
        project_id_or_key: str,
        body: UpdateDefaultProjectClassificationBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/project/{projectIdOrKey}/classification-level/default — Update the default data classification level of a project"""
        response = await self._request(
            'PUT',
            '/rest/api/3/project/{projectIdOrKey}/classification-level/default',
            path_params={'projectIdOrKey': project_id_or_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
