from __future__ import annotations

from typing import Any
from ..models.api import (
    Avatar,
    ProjectAvatars,
)
from .base import JiraBaseService


class ProjectAvatarsService(JiraBaseService):
    """Jira Cloud REST API v3 — Project avatars (4 operations)."""

    async def create_project_avatar(
        self,
        project_id_or_key: str,
        body: bytes,
        *,
        content_type: str = "image/png",
        x: int | None = None,
        y: int | None = None,
        size: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Avatar:
        """POST /rest/api/3/project/{projectIdOrKey}/avatar2 — Load project avatar"""
        response = await self._request(
            'POST',
            '/rest/api/3/project/{projectIdOrKey}/avatar2',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'x': x, 'y': y, 'size': size},
            headers={'X-Atlassian-Token': 'no-check'},
            body=body,
            content_type=content_type,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Avatar)

    async def delete_project_avatar(
        self,
        project_id_or_key: str,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/project/{projectIdOrKey}/avatar/{id} — Delete project avatar"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/project/{projectIdOrKey}/avatar/{id}',
            path_params={'projectIdOrKey': project_id_or_key, 'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_all_project_avatars(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectAvatars:
        """GET /rest/api/3/project/{projectIdOrKey}/avatars — Get all project avatars"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/avatars',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectAvatars)

    async def update_project_avatar(
        self,
        project_id_or_key: str,
        body: Avatar | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/project/{projectIdOrKey}/avatar — Set project avatar"""
        response = await self._request(
            'PUT',
            '/rest/api/3/project/{projectIdOrKey}/avatar',
            path_params={'projectIdOrKey': project_id_or_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
