from __future__ import annotations

from typing import Any
from ..models.api import (
    EntityProperty,
    PropertyKeys,
)
from .base import JiraBaseService


class UserPropertiesService(JiraBaseService):
    """Jira Cloud REST API v3 — User properties (4 operations)."""

    async def delete_user_property(
        self,
        property_key: str,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/user/properties/{propertyKey} — Delete user property"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/user/properties/{propertyKey}',
            path_params={'propertyKey': property_key},
            query_params={'accountId': account_id, 'userKey': user_key, 'username': username},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_user_property(
        self,
        property_key: str,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> EntityProperty:
        """GET /rest/api/3/user/properties/{propertyKey} — Get user property"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/properties/{propertyKey}',
            path_params={'propertyKey': property_key},
            query_params={'accountId': account_id, 'userKey': user_key, 'username': username},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, EntityProperty)

    async def get_user_property_keys(
        self,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PropertyKeys:
        """GET /rest/api/3/user/properties — Get user property keys"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/properties',
            query_params={'accountId': account_id, 'userKey': user_key, 'username': username},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PropertyKeys)

    async def set_user_property(
        self,
        property_key: str,
        body: Any,
        *,
        account_id: str | None = None,
        user_key: str | None = None,
        username: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/user/properties/{propertyKey} — Set user property"""
        response = await self._request(
            'PUT',
            '/rest/api/3/user/properties/{propertyKey}',
            path_params={'propertyKey': property_key},
            query_params={'accountId': account_id, 'userKey': user_key, 'username': username},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
