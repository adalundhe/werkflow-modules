from __future__ import annotations

from typing import Any
from ..models.api import (
    EntityProperty,
    ForgeAppPropertyKeysResponse,
    ForgeAppPropertyResponse,
    OperationMessage,
    PropertyKeys,
)
from .base import JiraBaseService


class AppPropertiesService(JiraBaseService):
    """Jira Cloud REST API v3 — App properties (8 operations)."""

    async def delete_addon_property(
        self,
        addon_key: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey} — Delete app property"""
        response = await self._request(
            'DELETE',
            '/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}',
            path_params={'addonKey': addon_key, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_addon_properties(
        self,
        addon_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PropertyKeys:
        """GET /rest/atlassian-connect/1/addons/{addonKey}/properties — Get app properties"""
        response = await self._request(
            'GET',
            '/rest/atlassian-connect/1/addons/{addonKey}/properties',
            path_params={'addonKey': addon_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PropertyKeys)

    async def get_addon_property(
        self,
        addon_key: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> EntityProperty:
        """GET /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey} — Get app property"""
        response = await self._request(
            'GET',
            '/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}',
            path_params={'addonKey': addon_key, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, EntityProperty)

    async def put_addon_property(
        self,
        addon_key: str,
        property_key: str,
        body: Any,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> OperationMessage:
        """PUT /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey} — Set app property"""
        response = await self._request(
            'PUT',
            '/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}',
            path_params={'addonKey': addon_key, 'propertyKey': property_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, OperationMessage)

    async def delete_forge_app_property(
        self,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/forge/1/app/properties/{propertyKey} — Delete app property (Forge)"""
        response = await self._request(
            'DELETE',
            '/rest/forge/1/app/properties/{propertyKey}',
            path_params={'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_forge_app_property(
        self,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ForgeAppPropertyResponse:
        """GET /rest/forge/1/app/properties/{propertyKey} — Get app property (Forge)"""
        response = await self._request(
            'GET',
            '/rest/forge/1/app/properties/{propertyKey}',
            path_params={'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ForgeAppPropertyResponse)

    async def get_forge_app_property_keys(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ForgeAppPropertyKeysResponse:
        """GET /rest/forge/1/app/properties — Get app property keys (Forge)"""
        response = await self._request(
            'GET',
            '/rest/forge/1/app/properties',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ForgeAppPropertyKeysResponse)

    async def put_forge_app_property(
        self,
        property_key: str,
        body: Any,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> OperationMessage:
        """PUT /rest/forge/1/app/properties/{propertyKey} — Set app property (Forge)"""
        response = await self._request(
            'PUT',
            '/rest/forge/1/app/properties/{propertyKey}',
            path_params={'propertyKey': property_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, OperationMessage)
