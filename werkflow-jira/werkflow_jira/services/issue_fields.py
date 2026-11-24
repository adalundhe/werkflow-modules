from __future__ import annotations

from typing import Any
from ..models.api import (
    CustomFieldDefinitionJsonBean,
    FieldDetails,
    PageBean2ProjectFieldBean,
    PageBeanContext,
    PageBeanField,
    PageBeanFieldProjectAssociation,
    UpdateCustomFieldDetails,
)
from .base import JiraBaseService


class IssueFieldsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue fields (11 operations)."""

    async def create_custom_field(
        self,
        body: CustomFieldDefinitionJsonBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> FieldDetails:
        """POST /rest/api/3/field — Create custom field"""
        response = await self._request(
            'POST',
            '/rest/api/3/field',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, FieldDetails)

    async def delete_custom_field(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/field/{id} — Delete custom field"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/field/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_contexts_for_field_deprecated(
        self,
        field_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanContext:
        """GET /rest/api/3/field/{fieldId}/contexts — Get contexts for a field"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldId}/contexts',
            path_params={'fieldId': field_id},
            query_params={'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanContext)

    async def get_field_project_associations(
        self,
        field_id: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanFieldProjectAssociation:
        """GET /rest/api/3/field/{fieldId}/association/project — Get field project associations"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldId}/association/project',
            path_params={'fieldId': field_id},
            query_params={'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanFieldProjectAssociation)

    async def get_fields(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[FieldDetails]:
        """GET /rest/api/3/field — Get fields"""
        response = await self._request(
            'GET',
            '/rest/api/3/field',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, FieldDetails)

    async def get_fields_paginated(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        type: list[str] | None = None,
        id: list[str] | None = None,
        query: str | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        project_ids: list[int] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanField:
        """GET /rest/api/3/field/search — Get fields paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/search',
            query_params={'startAt': start_at, 'maxResults': max_results, 'type': type, 'id': id, 'query': query, 'orderBy': order_by, 'expand': expand, 'projectIds': project_ids},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanField)

    async def get_project_fields(
        self,
        project_id: list[int],
        work_type_id: list[int],
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        field_id: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBean2ProjectFieldBean:
        """GET /rest/api/3/projects/fields — Get fields for projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/projects/fields',
            query_params={'startAt': start_at, 'maxResults': max_results, 'projectId': project_id, 'workTypeId': work_type_id, 'fieldId': field_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBean2ProjectFieldBean)

    async def get_trashed_fields_paginated(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id: list[str] | None = None,
        query: str | None = None,
        expand: str | None = None,
        order_by: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanField:
        """GET /rest/api/3/field/search/trashed — Get fields in trash paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/search/trashed',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'query': query, 'expand': expand, 'orderBy': order_by},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanField)

    async def restore_custom_field(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/field/{id}/restore — Restore custom field from trash"""
        response = await self._request(
            'POST',
            '/rest/api/3/field/{id}/restore',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def trash_custom_field(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/field/{id}/trash — Move custom field to trash"""
        response = await self._request(
            'POST',
            '/rest/api/3/field/{id}/trash',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_custom_field(
        self,
        field_id: str,
        body: UpdateCustomFieldDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/field/{fieldId} — Update custom field"""
        response = await self._request(
            'PUT',
            '/rest/api/3/field/{fieldId}',
            path_params={'fieldId': field_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
