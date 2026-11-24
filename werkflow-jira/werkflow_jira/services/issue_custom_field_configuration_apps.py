from __future__ import annotations

from typing import Any
from ..models.api import (
    ConfigurationsListParameters,
    CustomFieldConfigurations,
    PageBeanBulkContextualConfiguration,
    PageBeanContextualConfiguration,
)
from .base import JiraBaseService


class IssueCustomFieldConfigurationAppsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue custom field configuration (apps) (3 operations)."""

    async def get_custom_field_configuration(
        self,
        field_id_or_key: str,
        *,
        id: list[int] | None = None,
        field_context_id: list[int] | None = None,
        issue_id: int | None = None,
        project_key_or_id: str | None = None,
        issue_type_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanContextualConfiguration:
        """GET /rest/api/3/app/field/{fieldIdOrKey}/context/configuration — Get custom field configurations"""
        response = await self._request(
            'GET',
            '/rest/api/3/app/field/{fieldIdOrKey}/context/configuration',
            path_params={'fieldIdOrKey': field_id_or_key},
            query_params={'id': id, 'fieldContextId': field_context_id, 'issueId': issue_id, 'projectKeyOrId': project_key_or_id, 'issueTypeId': issue_type_id, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanContextualConfiguration)

    async def get_custom_fields_configurations(
        self,
        body: ConfigurationsListParameters | dict[str, Any],
        *,
        id: list[int] | None = None,
        field_context_id: list[int] | None = None,
        issue_id: int | None = None,
        project_key_or_id: str | None = None,
        issue_type_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanBulkContextualConfiguration:
        """POST /rest/api/3/app/field/context/configuration/list — Bulk get custom field configurations"""
        response = await self._request(
            'POST',
            '/rest/api/3/app/field/context/configuration/list',
            query_params={'id': id, 'fieldContextId': field_context_id, 'issueId': issue_id, 'projectKeyOrId': project_key_or_id, 'issueTypeId': issue_type_id, 'startAt': start_at, 'maxResults': max_results},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanBulkContextualConfiguration)

    async def update_custom_field_configuration(
        self,
        field_id_or_key: str,
        body: CustomFieldConfigurations | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/app/field/{fieldIdOrKey}/context/configuration — Update custom field configurations"""
        response = await self._request(
            'PUT',
            '/rest/api/3/app/field/{fieldIdOrKey}/context/configuration',
            path_params={'fieldIdOrKey': field_id_or_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
