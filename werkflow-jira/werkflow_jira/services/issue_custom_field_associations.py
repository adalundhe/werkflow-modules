from __future__ import annotations

from typing import Any
from ..models.api import (
    FieldAssociationsRequest,
)
from .base import JiraBaseService


class IssueCustomFieldAssociationsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue custom field associations (2 operations)."""

    async def create_associations(
        self,
        body: FieldAssociationsRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/field/association — Create associations"""
        response = await self._request(
            'PUT',
            '/rest/api/3/field/association',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def remove_associations(
        self,
        body: FieldAssociationsRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/field/association — Remove associations"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/field/association',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
