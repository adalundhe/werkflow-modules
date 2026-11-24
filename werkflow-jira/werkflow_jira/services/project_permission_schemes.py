from __future__ import annotations

from typing import Any
from ..models.api import (
    IdBean,
    PermissionScheme,
    ProjectIssueSecurityLevels,
    SecurityScheme,
)
from .base import JiraBaseService


class ProjectPermissionSchemesService(JiraBaseService):
    """Jira Cloud REST API v3 — Project permission schemes (4 operations)."""

    async def assign_permission_scheme(
        self,
        project_key_or_id: str,
        body: IdBean | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PermissionScheme:
        """PUT /rest/api/3/project/{projectKeyOrId}/permissionscheme — Assign permission scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/project/{projectKeyOrId}/permissionscheme',
            path_params={'projectKeyOrId': project_key_or_id},
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PermissionScheme)

    async def get_assigned_permission_scheme(
        self,
        project_key_or_id: str,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PermissionScheme:
        """GET /rest/api/3/project/{projectKeyOrId}/permissionscheme — Get assigned permission scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectKeyOrId}/permissionscheme',
            path_params={'projectKeyOrId': project_key_or_id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PermissionScheme)

    async def get_project_issue_security_scheme(
        self,
        project_key_or_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SecurityScheme:
        """GET /rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme — Get project issue security scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme',
            path_params={'projectKeyOrId': project_key_or_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SecurityScheme)

    async def get_security_levels_for_project(
        self,
        project_key_or_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectIssueSecurityLevels:
        """GET /rest/api/3/project/{projectKeyOrId}/securitylevel — Get project issue security levels"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectKeyOrId}/securitylevel',
            path_params={'projectKeyOrId': project_key_or_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectIssueSecurityLevels)
