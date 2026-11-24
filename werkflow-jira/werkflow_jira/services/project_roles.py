from __future__ import annotations

from typing import Any
from ..models.api import (
    CreateUpdateRoleRequestBean,
    ProjectRole,
    ProjectRoleDetails,
)
from .base import JiraBaseService


class ProjectRolesService(JiraBaseService):
    """Jira Cloud REST API v3 — Project roles (9 operations)."""

    async def create_project_role(
        self,
        body: CreateUpdateRoleRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectRole:
        """POST /rest/api/3/role — Create project role"""
        response = await self._request(
            'POST',
            '/rest/api/3/role',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectRole)

    async def delete_project_role(
        self,
        id: int,
        *,
        swap: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/role/{id} — Delete project role"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/role/{id}',
            path_params={'id': id},
            query_params={'swap': swap},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def fully_update_project_role(
        self,
        id: int,
        body: CreateUpdateRoleRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectRole:
        """PUT /rest/api/3/role/{id} — Fully update project role"""
        response = await self._request(
            'PUT',
            '/rest/api/3/role/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectRole)

    async def get_all_project_roles(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ProjectRole]:
        """GET /rest/api/3/role — Get all project roles"""
        response = await self._request(
            'GET',
            '/rest/api/3/role',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ProjectRole)

    async def get_project_role(
        self,
        project_id_or_key: str,
        id: int,
        *,
        exclude_inactive_users: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectRole:
        """GET /rest/api/3/project/{projectIdOrKey}/role/{id} — Get project role for project"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/role/{id}',
            path_params={'projectIdOrKey': project_id_or_key, 'id': id},
            query_params={'excludeInactiveUsers': exclude_inactive_users},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectRole)

    async def get_project_role_by_id(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectRole:
        """GET /rest/api/3/role/{id} — Get project role by ID"""
        response = await self._request(
            'GET',
            '/rest/api/3/role/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectRole)

    async def get_project_role_details(
        self,
        project_id_or_key: str,
        *,
        current_member: bool | None = None,
        exclude_connect_addons: bool | None = None,
        exclude_other_service_roles: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ProjectRoleDetails]:
        """GET /rest/api/3/project/{projectIdOrKey}/roledetails — Get project role details"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/roledetails',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'currentMember': current_member, 'excludeConnectAddons': exclude_connect_addons, 'excludeOtherServiceRoles': exclude_other_service_roles},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ProjectRoleDetails)

    async def get_project_roles(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> dict[str, str]:
        """GET /rest/api/3/project/{projectIdOrKey}/role — Get project roles for project"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/role',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def partial_update_project_role(
        self,
        id: int,
        body: CreateUpdateRoleRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectRole:
        """POST /rest/api/3/role/{id} — Partial update project role"""
        response = await self._request(
            'POST',
            '/rest/api/3/role/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectRole)
