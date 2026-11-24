from __future__ import annotations

from ..models.api import (
    AuditRecords,
)
from .base import JiraBaseService


class AuditRecordsService(JiraBaseService):
    """Jira Cloud REST API v3 — Audit records (1 operations)."""

    async def get_audit_records(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        filter: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> AuditRecords:
        """GET /rest/api/3/auditing/record — Get audit records"""
        response = await self._request(
            'GET',
            '/rest/api/3/auditing/record',
            query_params={'offset': offset, 'limit': limit, 'filter': filter, 'from': from_, 'to': to},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, AuditRecords)
