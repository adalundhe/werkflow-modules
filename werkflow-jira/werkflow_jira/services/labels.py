from __future__ import annotations

from ..models.api import (
    PageBeanString,
)
from .base import JiraBaseService


class LabelsService(JiraBaseService):
    """Jira Cloud REST API v3 — Labels (1 operations)."""

    async def get_all_labels(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        query: str | None = None,
        scope: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanString:
        """GET /rest/api/3/label — Get all labels"""
        response = await self._request(
            'GET',
            '/rest/api/3/label',
            query_params={'startAt': start_at, 'maxResults': max_results, 'query': query, 'scope': scope},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanString)
