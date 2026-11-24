from __future__ import annotations

from typing import Any
from ..models.api import (
    RemoteIssueLink,
    RemoteIssueLinkIdentifies,
    RemoteIssueLinkRequest,
)
from .base import JiraBaseService


class IssueRemoteLinksService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue remote links (6 operations)."""

    async def create_or_update_remote_issue_link(
        self,
        issue_id_or_key: str,
        body: RemoteIssueLinkRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> RemoteIssueLinkIdentifies:
        """POST /rest/api/3/issue/{issueIdOrKey}/remotelink — Create or update remote issue link"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/{issueIdOrKey}/remotelink',
            path_params={'issueIdOrKey': issue_id_or_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, RemoteIssueLinkIdentifies)

    async def delete_remote_issue_link_by_global_id(
        self,
        issue_id_or_key: str,
        global_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink — Delete remote issue link by global ID"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/{issueIdOrKey}/remotelink',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'globalId': global_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_remote_issue_link_by_id(
        self,
        issue_id_or_key: str,
        link_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId} — Delete remote issue link by ID"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}',
            path_params={'issueIdOrKey': issue_id_or_key, 'linkId': link_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_remote_issue_link_by_id(
        self,
        issue_id_or_key: str,
        link_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> RemoteIssueLink:
        """GET /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId} — Get remote issue link by ID"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}',
            path_params={'issueIdOrKey': issue_id_or_key, 'linkId': link_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, RemoteIssueLink)

    async def get_remote_issue_links(
        self,
        issue_id_or_key: str,
        *,
        global_id: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """GET /rest/api/3/issue/{issueIdOrKey}/remotelink — Get remote issue links"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/remotelink',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'globalId': global_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_remote_issue_link(
        self,
        issue_id_or_key: str,
        link_id: str,
        body: RemoteIssueLinkRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId} — Update remote issue link by ID"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}',
            path_params={'issueIdOrKey': issue_id_or_key, 'linkId': link_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
