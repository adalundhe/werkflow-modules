from __future__ import annotations

from typing import Any
from ..models.api import (
    DefaultShareScope,
    SharePermission,
    SharePermissionInputBean,
)
from .base import JiraBaseService


class FilterSharingService(JiraBaseService):
    """Jira Cloud REST API v3 — Filter sharing (6 operations)."""

    async def add_share_permission(
        self,
        id: int,
        body: SharePermissionInputBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[SharePermission]:
        """POST /rest/api/3/filter/{id}/permission — Add share permission"""
        response = await self._request(
            'POST',
            '/rest/api/3/filter/{id}/permission',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, SharePermission)

    async def delete_share_permission(
        self,
        id: int,
        permission_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/filter/{id}/permission/{permissionId} — Delete share permission"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/filter/{id}/permission/{permissionId}',
            path_params={'id': id, 'permissionId': permission_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_default_share_scope(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> DefaultShareScope:
        """GET /rest/api/3/filter/defaultShareScope — Get default share scope"""
        response = await self._request(
            'GET',
            '/rest/api/3/filter/defaultShareScope',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, DefaultShareScope)

    async def get_share_permission(
        self,
        id: int,
        permission_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SharePermission:
        """GET /rest/api/3/filter/{id}/permission/{permissionId} — Get share permission"""
        response = await self._request(
            'GET',
            '/rest/api/3/filter/{id}/permission/{permissionId}',
            path_params={'id': id, 'permissionId': permission_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SharePermission)

    async def get_share_permissions(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[SharePermission]:
        """GET /rest/api/3/filter/{id}/permission — Get share permissions"""
        response = await self._request(
            'GET',
            '/rest/api/3/filter/{id}/permission',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, SharePermission)

    async def set_default_share_scope(
        self,
        body: DefaultShareScope | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> DefaultShareScope:
        """PUT /rest/api/3/filter/defaultShareScope — Set default share scope"""
        response = await self._request(
            'PUT',
            '/rest/api/3/filter/defaultShareScope',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, DefaultShareScope)
