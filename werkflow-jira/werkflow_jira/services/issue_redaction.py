from __future__ import annotations

from typing import Any
from ..models.api import (
    BulkRedactionRequest,
    RedactionJobStatusResponse,
)
from .base import JiraBaseService


class IssueRedactionService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue redaction (2 operations)."""

    async def get_redaction_status(
        self,
        job_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> RedactionJobStatusResponse:
        """GET /rest/api/3/redact/status/{jobId} — Get redaction status"""
        response = await self._request(
            'GET',
            '/rest/api/3/redact/status/{jobId}',
            path_params={'jobId': job_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, RedactionJobStatusResponse)

    async def redact(
        self,
        body: BulkRedactionRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> str:
        """POST /rest/api/3/redact — Redact"""
        response = await self._request(
            'POST',
            '/rest/api/3/redact',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        payload = self._parse_json(response)
        return str(payload) if payload is not None else ""
