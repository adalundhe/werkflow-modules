from __future__ import annotations

from typing import Any
from ..models.api import (
    PermissionGrant,
    PermissionGrants,
    PermissionScheme,
    PermissionSchemes,
)
from .base import JiraBaseService


class PermissionSchemesService(JiraBaseService):
    """Jira Cloud REST API v3 — Permission schemes (9 operations)."""

    async def create_permission_grant(
        self,
        scheme_id: int,
        body: PermissionGrant | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PermissionGrant:
        """POST /rest/api/3/permissionscheme/{schemeId}/permission — Create permission grant"""
        response = await self._request(
            'POST',
            '/rest/api/3/permissionscheme/{schemeId}/permission',
            path_params={'schemeId': scheme_id},
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PermissionGrant)

    async def create_permission_scheme(
        self,
        body: PermissionScheme | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PermissionScheme:
        """POST /rest/api/3/permissionscheme — Create permission scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/permissionscheme',
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PermissionScheme)

    async def delete_permission_scheme(
        self,
        scheme_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/permissionscheme/{schemeId} — Delete permission scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/permissionscheme/{schemeId}',
            path_params={'schemeId': scheme_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_permission_scheme_entity(
        self,
        scheme_id: int,
        permission_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId} — Delete permission scheme grant"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}',
            path_params={'schemeId': scheme_id, 'permissionId': permission_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_all_permission_schemes(
        self,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PermissionSchemes:
        """GET /rest/api/3/permissionscheme — Get all permission schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/permissionscheme',
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PermissionSchemes)

    async def get_permission_scheme(
        self,
        scheme_id: int,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PermissionScheme:
        """GET /rest/api/3/permissionscheme/{schemeId} — Get permission scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/permissionscheme/{schemeId}',
            path_params={'schemeId': scheme_id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PermissionScheme)

    async def get_permission_scheme_grant(
        self,
        scheme_id: int,
        permission_id: int,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PermissionGrant:
        """GET /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId} — Get permission scheme grant"""
        response = await self._request(
            'GET',
            '/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}',
            path_params={'schemeId': scheme_id, 'permissionId': permission_id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PermissionGrant)

    async def get_permission_scheme_grants(
        self,
        scheme_id: int,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PermissionGrants:
        """GET /rest/api/3/permissionscheme/{schemeId}/permission — Get permission scheme grants"""
        response = await self._request(
            'GET',
            '/rest/api/3/permissionscheme/{schemeId}/permission',
            path_params={'schemeId': scheme_id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PermissionGrants)

    async def update_permission_scheme(
        self,
        scheme_id: int,
        body: PermissionScheme | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PermissionScheme:
        """PUT /rest/api/3/permissionscheme/{schemeId} — Update permission scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/permissionscheme/{schemeId}',
            path_params={'schemeId': scheme_id},
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PermissionScheme)
