from __future__ import annotations

from ..models.api import (
    Avatar,
    Avatars,
    SystemAvatars,
)
from .base import JiraBaseService


class AvatarsService(JiraBaseService):
    """Jira Cloud REST API v3 — Avatars (7 operations)."""

    async def delete_avatar(
        self,
        type: str,
        owning_object_id: str,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id} — Delete avatar"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}',
            path_params={'type': type, 'owningObjectId': owning_object_id, 'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_all_system_avatars(
        self,
        type: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SystemAvatars:
        """GET /rest/api/3/avatar/{type}/system — Get system avatars by type"""
        response = await self._request(
            'GET',
            '/rest/api/3/avatar/{type}/system',
            path_params={'type': type},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SystemAvatars)

    async def get_avatar_image_by_id(
        self,
        type: str,
        id: int,
        *,
        size: str | None = None,
        format: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> bytes:
        """GET /rest/api/3/universal_avatar/view/type/{type}/avatar/{id} — Get avatar image by ID"""
        response = await self._request(
            'GET',
            '/rest/api/3/universal_avatar/view/type/{type}/avatar/{id}',
            path_params={'type': type, 'id': id},
            query_params={'size': size, 'format': format},
            accept="*/*",
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_bytes(response)

    async def get_avatar_image_by_owner(
        self,
        type: str,
        entity_id: str,
        *,
        size: str | None = None,
        format: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> bytes:
        """GET /rest/api/3/universal_avatar/view/type/{type}/owner/{entityId} — Get avatar image by owner"""
        response = await self._request(
            'GET',
            '/rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}',
            path_params={'type': type, 'entityId': entity_id},
            query_params={'size': size, 'format': format},
            accept="*/*",
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_bytes(response)

    async def get_avatar_image_by_type(
        self,
        type: str,
        *,
        size: str | None = None,
        format: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> bytes:
        """GET /rest/api/3/universal_avatar/view/type/{type} — Get avatar image by type"""
        response = await self._request(
            'GET',
            '/rest/api/3/universal_avatar/view/type/{type}',
            path_params={'type': type},
            query_params={'size': size, 'format': format},
            accept="*/*",
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_bytes(response)

    async def get_avatars(
        self,
        type: str,
        entity_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Avatars:
        """GET /rest/api/3/universal_avatar/type/{type}/owner/{entityId} — Get avatars"""
        response = await self._request(
            'GET',
            '/rest/api/3/universal_avatar/type/{type}/owner/{entityId}',
            path_params={'type': type, 'entityId': entity_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Avatars)

    async def store_avatar(
        self,
        type: str,
        entity_id: str,
        body: bytes,
        size: int,
        *,
        content_type: str = "image/png",
        x: int | None = None,
        y: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Avatar:
        """POST /rest/api/3/universal_avatar/type/{type}/owner/{entityId} — Load avatar"""
        response = await self._request(
            'POST',
            '/rest/api/3/universal_avatar/type/{type}/owner/{entityId}',
            path_params={'type': type, 'entityId': entity_id},
            query_params={'x': x, 'y': y, 'size': size},
            headers={'X-Atlassian-Token': 'no-check'},
            body=body,
            content_type=content_type,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Avatar)
