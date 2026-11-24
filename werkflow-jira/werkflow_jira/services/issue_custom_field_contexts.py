from __future__ import annotations

from typing import Any
from ..models.api import (
    AddIssueTypesToContext,
    CreateCustomFieldContext,
    CustomFieldContextDefaultValueUpdate,
    CustomFieldContextDefaultValuesUpdate,
    CustomFieldContextUpdateDetails,
    IssueTypeIds,
    PageBeanContextDefaultValues,
    PageBeanContextForProjectAndIssueType,
    PageBeanCustomFieldContext,
    PageBeanCustomFieldContextDefaultValue,
    PageBeanCustomFieldContextProjectMapping,
    PageBeanIssueTypeToContextMapping,
    ProjectIds,
    ProjectIssueTypeMappings,
)
from .base import JiraBaseService


class IssueCustomFieldContextsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue custom field contexts (15 operations)."""

    async def add_issue_types_to_context(
        self,
        field_id: str,
        context_id: int,
        body: AddIssueTypesToContext | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/field/{fieldId}/context/{contextId}/issuetype — Add issue types to context"""
        response = await self._request(
            'PUT',
            '/rest/api/3/field/{fieldId}/context/{contextId}/issuetype',
            path_params={'fieldId': field_id, 'contextId': context_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def assign_projects_to_custom_field_context(
        self,
        field_id: str,
        context_id: int,
        body: ProjectIds | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/field/{fieldId}/context/{contextId}/project — Assign custom field context to projects"""
        response = await self._request(
            'PUT',
            '/rest/api/3/field/{fieldId}/context/{contextId}/project',
            path_params={'fieldId': field_id, 'contextId': context_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def create_custom_field_context(
        self,
        field_id: str,
        body: CreateCustomFieldContext | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> CreateCustomFieldContext:
        """POST /rest/api/3/field/{fieldId}/context — Create custom field context"""
        response = await self._request(
            'POST',
            '/rest/api/3/field/{fieldId}/context',
            path_params={'fieldId': field_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, CreateCustomFieldContext)

    async def delete_custom_field_context(
        self,
        field_id: str,
        context_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/field/{fieldId}/context/{contextId} — Delete custom field context"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/field/{fieldId}/context/{contextId}',
            path_params={'fieldId': field_id, 'contextId': context_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_context_default_values(
        self,
        field_id: str,
        *,
        context_id: list[int] | None = None,
        issue_type_id: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanContextDefaultValues:
        """GET /rest/api/3/field/{fieldId}/context/defaultValues — Get default values for a custom field grouped by context and issue type"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldId}/context/defaultValues',
            path_params={'fieldId': field_id},
            query_params={'contextId': context_id, 'issueTypeId': issue_type_id, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanContextDefaultValues)

    async def get_contexts_for_field(
        self,
        field_id: str,
        *,
        is_any_issue_type: bool | None = None,
        is_global_context: bool | None = None,
        context_id: list[int] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanCustomFieldContext:
        """GET /rest/api/3/field/{fieldId}/context — Get custom field contexts"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldId}/context',
            path_params={'fieldId': field_id},
            query_params={'isAnyIssueType': is_any_issue_type, 'isGlobalContext': is_global_context, 'contextId': context_id, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanCustomFieldContext)

    async def get_custom_field_contexts_for_projects_and_issue_types(
        self,
        field_id: str,
        body: ProjectIssueTypeMappings | dict[str, Any],
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanContextForProjectAndIssueType:
        """POST /rest/api/3/field/{fieldId}/context/mapping — Get custom field contexts for projects and issue types"""
        response = await self._request(
            'POST',
            '/rest/api/3/field/{fieldId}/context/mapping',
            path_params={'fieldId': field_id},
            query_params={'startAt': start_at, 'maxResults': max_results},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanContextForProjectAndIssueType)

    async def get_default_values(
        self,
        field_id: str,
        *,
        context_id: list[int] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanCustomFieldContextDefaultValue:
        """GET /rest/api/3/field/{fieldId}/context/defaultValue — Get custom field contexts default values"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldId}/context/defaultValue',
            path_params={'fieldId': field_id},
            query_params={'contextId': context_id, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanCustomFieldContextDefaultValue)

    async def get_issue_type_mappings_for_contexts(
        self,
        field_id: str,
        *,
        context_id: list[int] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueTypeToContextMapping:
        """GET /rest/api/3/field/{fieldId}/context/issuetypemapping — Get issue types for custom field context"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldId}/context/issuetypemapping',
            path_params={'fieldId': field_id},
            query_params={'contextId': context_id, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueTypeToContextMapping)

    async def get_project_context_mapping(
        self,
        field_id: str,
        *,
        context_id: list[int] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanCustomFieldContextProjectMapping:
        """GET /rest/api/3/field/{fieldId}/context/projectmapping — Get project mappings for custom field context"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldId}/context/projectmapping',
            path_params={'fieldId': field_id},
            query_params={'contextId': context_id, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanCustomFieldContextProjectMapping)

    async def remove_custom_field_context_from_projects(
        self,
        field_id: str,
        context_id: int,
        body: ProjectIds | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/field/{fieldId}/context/{contextId}/project/remove — Remove custom field context from projects"""
        response = await self._request(
            'POST',
            '/rest/api/3/field/{fieldId}/context/{contextId}/project/remove',
            path_params={'fieldId': field_id, 'contextId': context_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def remove_issue_types_from_context(
        self,
        field_id: str,
        context_id: int,
        body: IssueTypeIds | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove — Remove issue types from context"""
        response = await self._request(
            'POST',
            '/rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove',
            path_params={'fieldId': field_id, 'contextId': context_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def set_context_default_values(
        self,
        field_id: str,
        body: CustomFieldContextDefaultValuesUpdate | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/field/{fieldId}/context/defaultValues — Set default values for a custom field by context and issue type"""
        response = await self._request(
            'PUT',
            '/rest/api/3/field/{fieldId}/context/defaultValues',
            path_params={'fieldId': field_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def set_default_values(
        self,
        field_id: str,
        body: CustomFieldContextDefaultValueUpdate | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/field/{fieldId}/context/defaultValue — Set custom field contexts default values"""
        response = await self._request(
            'PUT',
            '/rest/api/3/field/{fieldId}/context/defaultValue',
            path_params={'fieldId': field_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_custom_field_context(
        self,
        field_id: str,
        context_id: int,
        body: CustomFieldContextUpdateDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/field/{fieldId}/context/{contextId} — Update custom field context"""
        response = await self._request(
            'PUT',
            '/rest/api/3/field/{fieldId}/context/{contextId}',
            path_params={'fieldId': field_id, 'contextId': context_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
