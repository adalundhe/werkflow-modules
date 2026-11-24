from __future__ import annotations

from typing import Any
from ..models.api import (
    CreateFieldAssociationSchemeRequest,
    CreateFieldAssociationSchemeResponse,
    DeleteFieldAssociationSchemeResponse,
    FieldSchemeToFieldsResponse,
    FieldSchemeToProjectsResponse,
    GetFieldAssociationParametersResponse,
    GetFieldAssociationSchemeByIdResponse,
    MinimalFieldSchemeToFieldsResponse,
    PageBean2FieldAssociationSchemeFieldSearchResult,
    PageBean2FieldAssociationSchemeProjectSearchResult,
    PageBean2GetFieldAssociationSchemeResponse,
    PageBean2GetProjectsWithFieldSchemesResponse,
    RemoveFieldParametersResult,
    UpdateFieldAssociationSchemeRequest,
    UpdateFieldAssociationSchemeResponse,
    UpdateFieldSchemeParametersResponse,
)
from .base import JiraBaseService


class FieldSchemesService(JiraBaseService):
    """Jira Cloud REST API v3 — Field schemes (15 operations)."""

    async def associate_projects_to_field_association_schemes(
        self,
        body: dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> FieldSchemeToProjectsResponse | None:
        """PUT /rest/api/3/config/fieldschemes/projects — Associate projects to field schemes"""
        response = await self._request(
            'PUT',
            '/rest/api/3/config/fieldschemes/projects',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_optional_model(response, FieldSchemeToProjectsResponse)

    async def clone_field_association_scheme(
        self,
        id: int,
        body: CreateFieldAssociationSchemeRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> CreateFieldAssociationSchemeResponse:
        """POST /rest/api/3/config/fieldschemes/{id}/clone — Clone field scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/config/fieldschemes/{id}/clone',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, CreateFieldAssociationSchemeResponse)

    async def create_field_association_scheme(
        self,
        body: CreateFieldAssociationSchemeRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> CreateFieldAssociationSchemeResponse:
        """POST /rest/api/3/config/fieldschemes — Create field scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/config/fieldschemes',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, CreateFieldAssociationSchemeResponse)

    async def delete_field_association_scheme(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> DeleteFieldAssociationSchemeResponse:
        """DELETE /rest/api/3/config/fieldschemes/{id} — Delete a field scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/config/fieldschemes/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, DeleteFieldAssociationSchemeResponse)

    async def get_field_association_scheme_by_id(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> GetFieldAssociationSchemeByIdResponse:
        """GET /rest/api/3/config/fieldschemes/{id} — Get field scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/config/fieldschemes/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, GetFieldAssociationSchemeByIdResponse)

    async def get_field_association_scheme_item_parameters(
        self,
        id: int,
        field_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> GetFieldAssociationParametersResponse:
        """GET /rest/api/3/config/fieldschemes/{id}/fields/{fieldId}/parameters — Get field parameters"""
        response = await self._request(
            'GET',
            '/rest/api/3/config/fieldschemes/{id}/fields/{fieldId}/parameters',
            path_params={'id': id, 'fieldId': field_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, GetFieldAssociationParametersResponse)

    async def get_field_association_schemes(
        self,
        *,
        project_id: list[int] | None = None,
        query: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBean2GetFieldAssociationSchemeResponse:
        """GET /rest/api/3/config/fieldschemes — Get field schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/config/fieldschemes',
            query_params={'projectId': project_id, 'query': query, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBean2GetFieldAssociationSchemeResponse)

    async def get_projects_with_field_schemes(
        self,
        project_id: list[int],
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBean2GetProjectsWithFieldSchemesResponse:
        """GET /rest/api/3/config/fieldschemes/projects — Get projects with field schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/config/fieldschemes/projects',
            query_params={'startAt': start_at, 'maxResults': max_results, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBean2GetProjectsWithFieldSchemesResponse)

    async def remove_field_association_scheme_item_parameters(
        self,
        body: dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> RemoveFieldParametersResult | None:
        """DELETE /rest/api/3/config/fieldschemes/fields/parameters — Remove field parameters"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/config/fieldschemes/fields/parameters',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_optional_model(response, RemoveFieldParametersResult)

    async def remove_fields_associated_with_schemes(
        self,
        body: dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> MinimalFieldSchemeToFieldsResponse | None:
        """DELETE /rest/api/3/config/fieldschemes/fields — Remove fields associated with field schemes"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/config/fieldschemes/fields',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_optional_model(response, MinimalFieldSchemeToFieldsResponse)

    async def search_field_association_scheme_fields(
        self,
        id: int,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        field_id: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBean2FieldAssociationSchemeFieldSearchResult:
        """GET /rest/api/3/config/fieldschemes/{id}/fields — Search field scheme fields"""
        response = await self._request(
            'GET',
            '/rest/api/3/config/fieldschemes/{id}/fields',
            path_params={'id': id},
            query_params={'startAt': start_at, 'maxResults': max_results, 'fieldId': field_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBean2FieldAssociationSchemeFieldSearchResult)

    async def search_field_association_scheme_projects(
        self,
        id: int,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: list[int] | None = None,
        query: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBean2FieldAssociationSchemeProjectSearchResult:
        """GET /rest/api/3/config/fieldschemes/{id}/projects — Search field scheme projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/config/fieldschemes/{id}/projects',
            path_params={'id': id},
            query_params={'startAt': start_at, 'maxResults': max_results, 'projectId': project_id, 'query': query},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBean2FieldAssociationSchemeProjectSearchResult)

    async def update_field_association_scheme(
        self,
        id: int,
        body: UpdateFieldAssociationSchemeRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> UpdateFieldAssociationSchemeResponse:
        """PUT /rest/api/3/config/fieldschemes/{id} — Update field scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/config/fieldschemes/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, UpdateFieldAssociationSchemeResponse)

    async def update_field_association_scheme_item_parameters(
        self,
        body: dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> UpdateFieldSchemeParametersResponse | None:
        """PUT /rest/api/3/config/fieldschemes/fields/parameters — Update field parameters"""
        response = await self._request(
            'PUT',
            '/rest/api/3/config/fieldschemes/fields/parameters',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_optional_model(response, UpdateFieldSchemeParametersResponse)

    async def update_fields_associated_with_schemes(
        self,
        body: dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> FieldSchemeToFieldsResponse | None:
        """PUT /rest/api/3/config/fieldschemes/fields — Update fields associated with field schemes"""
        response = await self._request(
            'PUT',
            '/rest/api/3/config/fieldschemes/fields',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_optional_model(response, FieldSchemeToFieldsResponse)
