from __future__ import annotations

from typing import Any
from ..models.api import (
    BulkAgentSessionsResponse,
    BulkStartAgentSessionsBatchRequest,
    BulkStartUniformAgentSessionsRequest,
)
from .base import JiraBaseService


class AgentsService(JiraBaseService):
    """Jira Cloud REST API v3 — Agents (2 operations)."""

    async def start_batch(
        self,
        body: BulkStartAgentSessionsBatchRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkAgentSessionsResponse:
        """POST /rest/api/3/agents/bulk/invoke/batch — Bulk start agent sessions (batch)"""
        response = await self._request(
            'POST',
            '/rest/api/3/agents/bulk/invoke/batch',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkAgentSessionsResponse)

    async def start_uniform(
        self,
        body: BulkStartUniformAgentSessionsRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkAgentSessionsResponse:
        """POST /rest/api/3/agents/bulk/invoke/uniform — Bulk start agent sessions (uniform)"""
        response = await self._request(
            'POST',
            '/rest/api/3/agents/bulk/invoke/uniform',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkAgentSessionsResponse)
