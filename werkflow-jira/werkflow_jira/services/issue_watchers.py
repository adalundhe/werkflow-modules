from __future__ import annotations

from typing import Any
from ..models.api import (
    BulkIssueIsWatching,
    IssueList,
    Watchers,
)
from .base import JiraBaseService


class IssueWatchersService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue watchers (4 operations)."""

    async def add_watcher(
        self,
        issue_id_or_key: str,
        body: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/issue/{issueIdOrKey}/watchers — Add watcher"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/{issueIdOrKey}/watchers',
            path_params={'issueIdOrKey': issue_id_or_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_is_watching_issue_bulk(
        self,
        body: IssueList | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkIssueIsWatching:
        """POST /rest/api/3/issue/watching — Get is watching issue bulk"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/watching',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkIssueIsWatching)

    async def get_issue_watchers(
        self,
        issue_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Watchers:
        """GET /rest/api/3/issue/{issueIdOrKey}/watchers — Get issue watchers"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/watchers',
            path_params={'issueIdOrKey': issue_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Watchers)

    async def remove_watcher(
        self,
        issue_id_or_key: str,
        *,
        username: str | None = None,
        account_id: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/{issueIdOrKey}/watchers — Delete watcher"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/{issueIdOrKey}/watchers',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'username': username, 'accountId': account_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None
