from __future__ import annotations

from typing import Any
from ..models.api import (
    CreateProjectDetails,
    IssueTypeWithStatus,
    NotificationScheme,
    PageBeanProject,
    Project,
    ProjectIdentifiers,
    ProjectIssueTypeHierarchy,
    UpdateProjectDetails,
)
from .base import JiraBaseService


class ProjectsService(JiraBaseService):
    """Jira Cloud REST API v3 — Projects (13 operations)."""

    async def archive_project(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/project/{projectIdOrKey}/archive — Archive project"""
        response = await self._request(
            'POST',
            '/rest/api/3/project/{projectIdOrKey}/archive',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def create_project(
        self,
        body: CreateProjectDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectIdentifiers:
        """POST /rest/api/3/project — Create project"""
        response = await self._request(
            'POST',
            '/rest/api/3/project',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectIdentifiers)

    async def delete_project(
        self,
        project_id_or_key: str,
        *,
        enable_undo: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/project/{projectIdOrKey} — Delete project"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/project/{projectIdOrKey}',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'enableUndo': enable_undo},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_project_asynchronously(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """POST /rest/api/3/project/{projectIdOrKey}/delete — Delete project asynchronously"""
        response = await self._request(
            'POST',
            '/rest/api/3/project/{projectIdOrKey}/delete',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_all_projects(
        self,
        *,
        expand: str | None = None,
        recent: int | None = None,
        properties: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[Project]:
        """GET /rest/api/3/project — Get all projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/project',
            query_params={'expand': expand, 'recent': recent, 'properties': properties},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, Project)

    async def get_all_statuses(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[IssueTypeWithStatus]:
        """GET /rest/api/3/project/{projectIdOrKey}/statuses — Get all statuses for project"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/statuses',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, IssueTypeWithStatus)

    async def get_hierarchy(
        self,
        project_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectIssueTypeHierarchy:
        """GET /rest/api/3/project/{projectId}/hierarchy — Get project issue type hierarchy"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectId}/hierarchy',
            path_params={'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectIssueTypeHierarchy)

    async def get_notification_scheme_for_project(
        self,
        project_key_or_id: str,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> NotificationScheme:
        """GET /rest/api/3/project/{projectKeyOrId}/notificationscheme — Get project notification scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectKeyOrId}/notificationscheme',
            path_params={'projectKeyOrId': project_key_or_id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, NotificationScheme)

    async def get_project(
        self,
        project_id_or_key: str,
        *,
        expand: str | None = None,
        properties: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Project:
        """GET /rest/api/3/project/{projectIdOrKey} — Get project"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'expand': expand, 'properties': properties},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Project)

    async def get_recent(
        self,
        *,
        expand: str | None = None,
        properties: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[Project]:
        """GET /rest/api/3/project/recent — Get recent projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/recent',
            query_params={'expand': expand, 'properties': properties},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, Project)

    async def restore(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Project:
        """POST /rest/api/3/project/{projectIdOrKey}/restore — Restore deleted or archived project"""
        response = await self._request(
            'POST',
            '/rest/api/3/project/{projectIdOrKey}/restore',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Project)

    async def search_projects(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        id: list[int] | None = None,
        keys: list[str] | None = None,
        query: str | None = None,
        type_key: str | None = None,
        category_id: int | None = None,
        action: str | None = None,
        expand: str | None = None,
        status: list[str] | None = None,
        properties: list[str] | None = None,
        property_query: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanProject:
        """GET /rest/api/3/project/search — Get projects paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/search',
            query_params={'startAt': start_at, 'maxResults': max_results, 'orderBy': order_by, 'id': id, 'keys': keys, 'query': query, 'typeKey': type_key, 'categoryId': category_id, 'action': action, 'expand': expand, 'status': status, 'properties': properties, 'propertyQuery': property_query},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanProject)

    async def update_project(
        self,
        project_id_or_key: str,
        body: UpdateProjectDetails | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Project:
        """PUT /rest/api/3/project/{projectIdOrKey} — Update project"""
        response = await self._request(
            'PUT',
            '/rest/api/3/project/{projectIdOrKey}',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Project)
