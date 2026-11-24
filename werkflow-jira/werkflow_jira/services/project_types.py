from __future__ import annotations

from ..models.api import (
    ProjectType,
)
from .base import JiraBaseService


class ProjectTypesService(JiraBaseService):
    """Jira Cloud REST API v3 — Project types (4 operations)."""

    async def get_accessible_project_type_by_key(
        self,
        project_type_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectType:
        """GET /rest/api/3/project/type/{projectTypeKey}/accessible — Get accessible project type by key"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/type/{projectTypeKey}/accessible',
            path_params={'projectTypeKey': project_type_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectType)

    async def get_all_accessible_project_types(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ProjectType]:
        """GET /rest/api/3/project/type/accessible — Get licensed project types"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/type/accessible',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ProjectType)

    async def get_all_project_types(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ProjectType]:
        """GET /rest/api/3/project/type — Get all project types"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/type',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ProjectType)

    async def get_project_type_by_key(
        self,
        project_type_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectType:
        """GET /rest/api/3/project/type/{projectTypeKey} — Get project type by key"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/type/{projectTypeKey}',
            path_params={'projectTypeKey': project_type_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectType)
