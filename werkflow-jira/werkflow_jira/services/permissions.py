from __future__ import annotations

from typing import Any
from ..models.api import (
    BulkPermissionGrants,
    BulkPermissionsRequestBean,
    Permissions,
    PermissionsKeysBean,
    PermittedProjects,
)
from .base import JiraBaseService


class PermissionsService(JiraBaseService):
    """Jira Cloud REST API v3 — Permissions (4 operations)."""

    async def get_all_permissions(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Permissions:
        """GET /rest/api/3/permissions — Get all permissions"""
        response = await self._request(
            'GET',
            '/rest/api/3/permissions',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Permissions)

    async def get_bulk_permissions(
        self,
        body: BulkPermissionsRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkPermissionGrants:
        """POST /rest/api/3/permissions/check — Get bulk permissions"""
        response = await self._request(
            'POST',
            '/rest/api/3/permissions/check',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkPermissionGrants)

    async def get_my_permissions(
        self,
        *,
        project_key: str | None = None,
        project_id: str | None = None,
        issue_key: str | None = None,
        issue_id: str | None = None,
        permissions: str | None = None,
        project_uuid: str | None = None,
        project_configuration_uuid: str | None = None,
        comment_id: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Permissions:
        """GET /rest/api/3/mypermissions — Get my permissions"""
        response = await self._request(
            'GET',
            '/rest/api/3/mypermissions',
            query_params={'projectKey': project_key, 'projectId': project_id, 'issueKey': issue_key, 'issueId': issue_id, 'permissions': permissions, 'projectUuid': project_uuid, 'projectConfigurationUuid': project_configuration_uuid, 'commentId': comment_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Permissions)

    async def get_permitted_projects(
        self,
        body: PermissionsKeysBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PermittedProjects:
        """POST /rest/api/3/permissions/project — Get permitted projects"""
        response = await self._request(
            'POST',
            '/rest/api/3/permissions/project',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PermittedProjects)
