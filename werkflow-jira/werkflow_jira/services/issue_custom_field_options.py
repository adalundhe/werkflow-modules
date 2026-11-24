from __future__ import annotations

from typing import Any
from ..models.api import (
    BulkCustomFieldOptionCreateRequest,
    BulkCustomFieldOptionUpdateRequest,
    CustomFieldCreatedContextOptionsList,
    CustomFieldOption,
    CustomFieldUpdatedContextOptionsList,
    OrderOfCustomFieldOptions,
    PageBeanCustomFieldContextOption,
)
from .base import JiraBaseService


class IssueCustomFieldOptionsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue custom field options (7 operations)."""

    async def create_custom_field_option(
        self,
        field_id: str,
        context_id: int,
        body: BulkCustomFieldOptionCreateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> CustomFieldCreatedContextOptionsList:
        """POST /rest/api/3/field/{fieldId}/context/{contextId}/option — Create custom field options (context)"""
        response = await self._request(
            'POST',
            '/rest/api/3/field/{fieldId}/context/{contextId}/option',
            path_params={'fieldId': field_id, 'contextId': context_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, CustomFieldCreatedContextOptionsList)

    async def delete_custom_field_option(
        self,
        field_id: str,
        context_id: int,
        option_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId} — Delete custom field options (context)"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}',
            path_params={'fieldId': field_id, 'contextId': context_id, 'optionId': option_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_custom_field_option(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> CustomFieldOption:
        """GET /rest/api/3/customFieldOption/{id} — Get custom field option"""
        response = await self._request(
            'GET',
            '/rest/api/3/customFieldOption/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, CustomFieldOption)

    async def get_options_for_context(
        self,
        field_id: str,
        context_id: int,
        *,
        option_id: int | None = None,
        query: str | None = None,
        only_options: bool | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanCustomFieldContextOption:
        """GET /rest/api/3/field/{fieldId}/context/{contextId}/option — Get custom field options (context)"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldId}/context/{contextId}/option',
            path_params={'fieldId': field_id, 'contextId': context_id},
            query_params={'optionId': option_id, 'query': query, 'onlyOptions': only_options, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanCustomFieldContextOption)

    async def reorder_custom_field_options(
        self,
        field_id: str,
        context_id: int,
        body: OrderOfCustomFieldOptions | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/field/{fieldId}/context/{contextId}/option/move — Reorder custom field options (context)"""
        response = await self._request(
            'PUT',
            '/rest/api/3/field/{fieldId}/context/{contextId}/option/move',
            path_params={'fieldId': field_id, 'contextId': context_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def replace_custom_field_option(
        self,
        field_id: str,
        option_id: int,
        context_id: int,
        *,
        replace_with: int | None = None,
        jql: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue — Replace custom field options"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue',
            path_params={'fieldId': field_id, 'optionId': option_id, 'contextId': context_id},
            query_params={'replaceWith': replace_with, 'jql': jql},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def update_custom_field_option(
        self,
        field_id: str,
        context_id: int,
        body: BulkCustomFieldOptionUpdateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> CustomFieldUpdatedContextOptionsList:
        """PUT /rest/api/3/field/{fieldId}/context/{contextId}/option — Update custom field options (context)"""
        response = await self._request(
            'PUT',
            '/rest/api/3/field/{fieldId}/context/{contextId}/option',
            path_params={'fieldId': field_id, 'contextId': context_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, CustomFieldUpdatedContextOptionsList)
