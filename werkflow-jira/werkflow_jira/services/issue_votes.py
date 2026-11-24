from __future__ import annotations

from typing import Any
from ..models.api import (
    Votes,
)
from .base import JiraBaseService


class IssueVotesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue votes (3 operations)."""

    async def add_vote(
        self,
        issue_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/issue/{issueIdOrKey}/votes — Add vote"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/{issueIdOrKey}/votes',
            path_params={'issueIdOrKey': issue_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_votes(
        self,
        issue_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Votes:
        """GET /rest/api/3/issue/{issueIdOrKey}/votes — Get votes"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/votes',
            path_params={'issueIdOrKey': issue_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Votes)

    async def remove_vote(
        self,
        issue_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/{issueIdOrKey}/votes — Delete vote"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/{issueIdOrKey}/votes',
            path_params={'issueIdOrKey': issue_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None
