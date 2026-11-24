from __future__ import annotations

from typing import Any
from ..models.api import (
    EntityProperty,
    PropertyKeys,
)
from .base import JiraBaseService


class IssueTypePropertiesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue type properties (4 operations)."""

    async def delete_issue_type_property(
        self,
        issue_type_id: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey} — Delete issue type property"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}',
            path_params={'issueTypeId': issue_type_id, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_issue_type_property(
        self,
        issue_type_id: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> EntityProperty:
        """GET /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey} — Get issue type property"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}',
            path_params={'issueTypeId': issue_type_id, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, EntityProperty)

    async def get_issue_type_property_keys(
        self,
        issue_type_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PropertyKeys:
        """GET /rest/api/3/issuetype/{issueTypeId}/properties — Get issue type property keys"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetype/{issueTypeId}/properties',
            path_params={'issueTypeId': issue_type_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PropertyKeys)

    async def set_issue_type_property(
        self,
        issue_type_id: str,
        property_key: str,
        body: Any,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey} — Set issue type property"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}',
            path_params={'issueTypeId': issue_type_id, 'propertyKey': property_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
