from __future__ import annotations

from typing import Any
from ..models.api import (
    ConnectCustomFieldValues,
    EntityPropertyDetails,
    WorkflowRulesSearch,
    WorkflowRulesSearchDetails,
)
from .base import JiraBaseService


class AppMigrationService(JiraBaseService):
    """Jira Cloud REST API v3 — App migration (3 operations)."""

    async def update_issue_fields(
        self,
        body: ConnectCustomFieldValues | dict[str, Any],
        atlassian_transfer_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/atlassian-connect/1/migration/field — Bulk update custom field value"""
        response = await self._request(
            'PUT',
            '/rest/atlassian-connect/1/migration/field',
            headers={'Atlassian-Transfer-Id': atlassian_transfer_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_entity_properties_value(
        self,
        entity_type: str,
        body: list[EntityPropertyDetails | dict[str, Any]],
        atlassian_transfer_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """PUT /rest/atlassian-connect/1/migration/properties/{entityType} — Bulk update entity properties"""
        response = await self._request(
            'PUT',
            '/rest/atlassian-connect/1/migration/properties/{entityType}',
            path_params={'entityType': entity_type},
            headers={'Atlassian-Transfer-Id': atlassian_transfer_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def workflow_rule_search(
        self,
        body: WorkflowRulesSearch | dict[str, Any],
        atlassian_transfer_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowRulesSearchDetails:
        """POST /rest/atlassian-connect/1/migration/workflow/rule/search — Get workflow transition rule configurations"""
        response = await self._request(
            'POST',
            '/rest/atlassian-connect/1/migration/workflow/rule/search',
            headers={'Atlassian-Transfer-Id': atlassian_transfer_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowRulesSearchDetails)
