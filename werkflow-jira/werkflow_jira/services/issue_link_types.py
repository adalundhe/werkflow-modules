from __future__ import annotations

from typing import Any
from ..models.api import (
    IssueLinkType,
    IssueLinkTypes,
)
from .base import JiraBaseService


class IssueLinkTypesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue link types (5 operations)."""

    async def create_issue_link_type(
        self,
        body: IssueLinkType | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueLinkType:
        """POST /rest/api/3/issueLinkType — Create issue link type"""
        response = await self._request(
            'POST',
            '/rest/api/3/issueLinkType',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueLinkType)

    async def delete_issue_link_type(
        self,
        issue_link_type_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issueLinkType/{issueLinkTypeId} — Delete issue link type"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issueLinkType/{issueLinkTypeId}',
            path_params={'issueLinkTypeId': issue_link_type_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_issue_link_type(
        self,
        issue_link_type_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueLinkType:
        """GET /rest/api/3/issueLinkType/{issueLinkTypeId} — Get issue link type"""
        response = await self._request(
            'GET',
            '/rest/api/3/issueLinkType/{issueLinkTypeId}',
            path_params={'issueLinkTypeId': issue_link_type_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueLinkType)

    async def get_issue_link_types(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueLinkTypes:
        """GET /rest/api/3/issueLinkType — Get issue link types"""
        response = await self._request(
            'GET',
            '/rest/api/3/issueLinkType',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueLinkTypes)

    async def update_issue_link_type(
        self,
        issue_link_type_id: str,
        body: IssueLinkType | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueLinkType:
        """PUT /rest/api/3/issueLinkType/{issueLinkTypeId} — Update issue link type"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issueLinkType/{issueLinkTypeId}',
            path_params={'issueLinkTypeId': issue_link_type_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueLinkType)
