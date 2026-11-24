from __future__ import annotations

from ..models.api import (
    PageBeanIssueSecurityLevelMember,
    SecurityLevel,
)
from .base import JiraBaseService


class IssueSecurityLevelService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue security level (2 operations)."""

    async def get_issue_security_level(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SecurityLevel:
        """GET /rest/api/3/securitylevel/{id} — Get issue security level"""
        response = await self._request(
            'GET',
            '/rest/api/3/securitylevel/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SecurityLevel)

    async def get_issue_security_level_members(
        self,
        issue_security_scheme_id: int,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_security_level_id: list[str] | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueSecurityLevelMember:
        """GET /rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members — Get issue security level members by issue security scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members',
            path_params={'issueSecuritySchemeId': issue_security_scheme_id},
            query_params={'startAt': start_at, 'maxResults': max_results, 'issueSecurityLevelId': issue_security_level_id, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueSecurityLevelMember)
