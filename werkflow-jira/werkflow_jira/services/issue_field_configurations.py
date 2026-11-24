from __future__ import annotations

from typing import Any
from ..models.api import (
    AssociateFieldConfigurationsWithIssueTypesRequest,
    FieldConfiguration,
    FieldConfigurationDetails,
    FieldConfigurationItemsDetails,
    FieldConfigurationScheme,
    FieldConfigurationSchemeProjectAssociation,
    IssueTypeIdsToRemove,
    PageBeanFieldConfigurationDetails,
    PageBeanFieldConfigurationIssueTypeItem,
    PageBeanFieldConfigurationItem,
    PageBeanFieldConfigurationScheme,
    PageBeanFieldConfigurationSchemeProjects,
    UpdateFieldConfigurationSchemeDetails,
)
from .base import JiraBaseService


class IssueFieldConfigurationsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue field configurations (15 operations)."""

    async def assign_field_configuration_scheme_to_project(
        self,
        body: FieldConfigurationSchemeProjectAssociation | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/fieldconfigurationscheme/project — Assign field configuration scheme to project"""
        response = await self._request(
            'PUT',
            '/rest/api/3/fieldconfigurationscheme/project',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def create_field_configuration(
        self,
        body: FieldConfigurationDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> FieldConfiguration:
        """POST /rest/api/3/fieldconfiguration — Create field configuration"""
        response = await self._request(
            'POST',
            '/rest/api/3/fieldconfiguration',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, FieldConfiguration)

    async def create_field_configuration_scheme(
        self,
        body: UpdateFieldConfigurationSchemeDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> FieldConfigurationScheme:
        """POST /rest/api/3/fieldconfigurationscheme — Create field configuration scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/fieldconfigurationscheme',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, FieldConfigurationScheme)

    async def delete_field_configuration(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/fieldconfiguration/{id} — Delete field configuration"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/fieldconfiguration/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def delete_field_configuration_scheme(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/fieldconfigurationscheme/{id} — Delete field configuration scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/fieldconfigurationscheme/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_all_field_configuration_schemes(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id: list[int] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanFieldConfigurationScheme:
        """GET /rest/api/3/fieldconfigurationscheme — Get all field configuration schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/fieldconfigurationscheme',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanFieldConfigurationScheme)

    async def get_all_field_configurations(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id: list[int] | None = None,
        is_default: bool | None = None,
        query: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanFieldConfigurationDetails:
        """GET /rest/api/3/fieldconfiguration — Get all field configurations"""
        response = await self._request(
            'GET',
            '/rest/api/3/fieldconfiguration',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'isDefault': is_default, 'query': query},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanFieldConfigurationDetails)

    async def get_field_configuration_items(
        self,
        id: int,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanFieldConfigurationItem:
        """GET /rest/api/3/fieldconfiguration/{id}/fields — Get field configuration items"""
        response = await self._request(
            'GET',
            '/rest/api/3/fieldconfiguration/{id}/fields',
            path_params={'id': id},
            query_params={'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanFieldConfigurationItem)

    async def get_field_configuration_scheme_mappings(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        field_configuration_scheme_id: list[int] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanFieldConfigurationIssueTypeItem:
        """GET /rest/api/3/fieldconfigurationscheme/mapping — Get field configuration issue type items"""
        response = await self._request(
            'GET',
            '/rest/api/3/fieldconfigurationscheme/mapping',
            query_params={'startAt': start_at, 'maxResults': max_results, 'fieldConfigurationSchemeId': field_configuration_scheme_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanFieldConfigurationIssueTypeItem)

    async def get_field_configuration_scheme_project_mapping(
        self,
        project_id: list[int],
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanFieldConfigurationSchemeProjects:
        """GET /rest/api/3/fieldconfigurationscheme/project — Get field configuration schemes for projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/fieldconfigurationscheme/project',
            query_params={'startAt': start_at, 'maxResults': max_results, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanFieldConfigurationSchemeProjects)

    async def remove_issue_types_from_global_field_configuration_scheme(
        self,
        id: int,
        body: IssueTypeIdsToRemove | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/fieldconfigurationscheme/{id}/mapping/delete — Remove issue types from field configuration scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/fieldconfigurationscheme/{id}/mapping/delete',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def set_field_configuration_scheme_mapping(
        self,
        id: int,
        body: AssociateFieldConfigurationsWithIssueTypesRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/fieldconfigurationscheme/{id}/mapping — Assign issue types to field configurations"""
        response = await self._request(
            'PUT',
            '/rest/api/3/fieldconfigurationscheme/{id}/mapping',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_field_configuration(
        self,
        id: int,
        body: FieldConfigurationDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/fieldconfiguration/{id} — Update field configuration"""
        response = await self._request(
            'PUT',
            '/rest/api/3/fieldconfiguration/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_field_configuration_items(
        self,
        id: int,
        body: FieldConfigurationItemsDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/fieldconfiguration/{id}/fields — Update field configuration items"""
        response = await self._request(
            'PUT',
            '/rest/api/3/fieldconfiguration/{id}/fields',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_field_configuration_scheme(
        self,
        id: int,
        body: UpdateFieldConfigurationSchemeDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/fieldconfigurationscheme/{id} — Update field configuration scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/fieldconfigurationscheme/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
