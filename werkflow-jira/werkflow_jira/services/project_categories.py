from __future__ import annotations

from typing import Any
from ..models.api import (
    ProjectCategory,
    UpdatedProjectCategory,
)
from .base import JiraBaseService


class ProjectCategoriesService(JiraBaseService):
    """Jira Cloud REST API v3 — Project categories (5 operations)."""

    async def create_project_category(
        self,
        body: ProjectCategory | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectCategory:
        """POST /rest/api/3/projectCategory — Create project category"""
        response = await self._request(
            'POST',
            '/rest/api/3/projectCategory',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectCategory)

    async def get_all_project_categories(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ProjectCategory]:
        """GET /rest/api/3/projectCategory — Get all project categories"""
        response = await self._request(
            'GET',
            '/rest/api/3/projectCategory',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ProjectCategory)

    async def get_project_category_by_id(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectCategory:
        """GET /rest/api/3/projectCategory/{id} — Get project category by ID"""
        response = await self._request(
            'GET',
            '/rest/api/3/projectCategory/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectCategory)

    async def remove_project_category(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/projectCategory/{id} — Delete project category"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/projectCategory/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def update_project_category(
        self,
        id: int,
        body: ProjectCategory | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> UpdatedProjectCategory:
        """PUT /rest/api/3/projectCategory/{id} — Update project category"""
        response = await self._request(
            'PUT',
            '/rest/api/3/projectCategory/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, UpdatedProjectCategory)
