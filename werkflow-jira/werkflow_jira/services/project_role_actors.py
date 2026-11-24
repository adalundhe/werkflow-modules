from __future__ import annotations

from typing import Any
from ..models.api import (
    ActorInputBean,
    ActorsMap,
    ProjectRole,
    ProjectRoleActorsUpdateBean,
)
from .base import JiraBaseService


class ProjectRoleActorsService(JiraBaseService):
    """Jira Cloud REST API v3 — Project role actors (6 operations)."""

    async def add_actor_users(
        self,
        project_id_or_key: str,
        id: int,
        body: ActorsMap | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectRole:
        """POST /rest/api/3/project/{projectIdOrKey}/role/{id} — Add actors to project role"""
        response = await self._request(
            'POST',
            '/rest/api/3/project/{projectIdOrKey}/role/{id}',
            path_params={'projectIdOrKey': project_id_or_key, 'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectRole)

    async def add_project_role_actors_to_role(
        self,
        id: int,
        body: ActorInputBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectRole:
        """POST /rest/api/3/role/{id}/actors — Add default actors to project role"""
        response = await self._request(
            'POST',
            '/rest/api/3/role/{id}/actors',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectRole)

    async def delete_actor(
        self,
        project_id_or_key: str,
        id: int,
        *,
        user: str | None = None,
        group: str | None = None,
        group_id: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/project/{projectIdOrKey}/role/{id} — Delete actors from project role"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/project/{projectIdOrKey}/role/{id}',
            path_params={'projectIdOrKey': project_id_or_key, 'id': id},
            query_params={'user': user, 'group': group, 'groupId': group_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_project_role_actors_from_role(
        self,
        id: int,
        *,
        user: str | None = None,
        group_id: str | None = None,
        group: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectRole:
        """DELETE /rest/api/3/role/{id}/actors — Delete default actors from project role"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/role/{id}/actors',
            path_params={'id': id},
            query_params={'user': user, 'groupId': group_id, 'group': group},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectRole)

    async def get_project_role_actors_for_role(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectRole:
        """GET /rest/api/3/role/{id}/actors — Get default actors for project role"""
        response = await self._request(
            'GET',
            '/rest/api/3/role/{id}/actors',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectRole)

    async def set_actors(
        self,
        project_id_or_key: str,
        id: int,
        body: ProjectRoleActorsUpdateBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectRole:
        """PUT /rest/api/3/project/{projectIdOrKey}/role/{id} — Set actors for project role"""
        response = await self._request(
            'PUT',
            '/rest/api/3/project/{projectIdOrKey}/role/{id}',
            path_params={'projectIdOrKey': project_id_or_key, 'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectRole)
