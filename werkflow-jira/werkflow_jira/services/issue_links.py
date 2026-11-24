from __future__ import annotations

from typing import Any
from ..models.api import (
    IssueLink,
    LinkIssueRequestJsonBean,
)
from .base import JiraBaseService


class IssueLinksService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue links (3 operations)."""

    async def delete_issue_link(
        self,
        link_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issueLink/{linkId} — Delete issue link"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issueLink/{linkId}',
            path_params={'linkId': link_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_issue_link(
        self,
        link_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueLink:
        """GET /rest/api/3/issueLink/{linkId} — Get issue link"""
        response = await self._request(
            'GET',
            '/rest/api/3/issueLink/{linkId}',
            path_params={'linkId': link_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueLink)

    async def link_issues(
        self,
        body: LinkIssueRequestJsonBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/issueLink — Create issue link"""
        response = await self._request(
            'POST',
            '/rest/api/3/issueLink',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
