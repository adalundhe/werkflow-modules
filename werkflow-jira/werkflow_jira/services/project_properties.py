from __future__ import annotations

from typing import Any
from ..models.api import (
    EntityProperty,
    PropertyKeys,
)
from .base import JiraBaseService


class ProjectPropertiesService(JiraBaseService):
    """Jira Cloud REST API v3 — Project properties (4 operations)."""

    async def delete_project_property(
        self,
        project_id_or_key: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey} — Delete project property"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}',
            path_params={'projectIdOrKey': project_id_or_key, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_project_property(
        self,
        project_id_or_key: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> EntityProperty:
        """GET /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey} — Get project property"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}',
            path_params={'projectIdOrKey': project_id_or_key, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, EntityProperty)

    async def get_project_property_keys(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PropertyKeys:
        """GET /rest/api/3/project/{projectIdOrKey}/properties — Get project property keys"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/properties',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PropertyKeys)

    async def set_project_property(
        self,
        project_id_or_key: str,
        property_key: str,
        body: Any,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey} — Set project property"""
        response = await self._request(
            'PUT',
            '/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}',
            path_params={'projectIdOrKey': project_id_or_key, 'propertyKey': property_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
