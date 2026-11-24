from __future__ import annotations

from typing import Any
from ..models.api import (
    Avatar,
    IssueTypeCreateBean,
    IssueTypeDetails,
    IssueTypeUpdateBean,
)
from .base import JiraBaseService


class IssueTypesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue types (8 operations)."""

    async def create_issue_type(
        self,
        body: IssueTypeCreateBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueTypeDetails:
        """POST /rest/api/3/issuetype — Create issue type"""
        response = await self._request(
            'POST',
            '/rest/api/3/issuetype',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueTypeDetails)

    async def create_issue_type_avatar(
        self,
        id: str,
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
        """POST /rest/api/3/issuetype/{id}/avatar2 — Load issue type avatar"""
        response = await self._request(
            'POST',
            '/rest/api/3/issuetype/{id}/avatar2',
            path_params={'id': id},
            query_params={'x': x, 'y': y, 'size': size},
            headers={'X-Atlassian-Token': 'no-check'},
            body=body,
            content_type=content_type,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Avatar)

    async def delete_issue_type(
        self,
        id: str,
        *,
        alternative_issue_type_id: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issuetype/{id} — Delete issue type"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issuetype/{id}',
            path_params={'id': id},
            query_params={'alternativeIssueTypeId': alternative_issue_type_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_alternative_issue_types(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[IssueTypeDetails]:
        """GET /rest/api/3/issuetype/{id}/alternatives — Get alternative issue types"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetype/{id}/alternatives',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, IssueTypeDetails)

    async def get_issue_all_types(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[IssueTypeDetails]:
        """GET /rest/api/3/issuetype — Get all issue types for user"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetype',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, IssueTypeDetails)

    async def get_issue_type(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueTypeDetails:
        """GET /rest/api/3/issuetype/{id} — Get issue type"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetype/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueTypeDetails)

    async def get_issue_types_for_project(
        self,
        project_id: int,
        *,
        level: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[IssueTypeDetails]:
        """GET /rest/api/3/issuetype/project — Get issue types for project"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetype/project',
            query_params={'projectId': project_id, 'level': level},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, IssueTypeDetails)

    async def update_issue_type(
        self,
        id: str,
        body: IssueTypeUpdateBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueTypeDetails:
        """PUT /rest/api/3/issuetype/{id} — Update issue type"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuetype/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueTypeDetails)
