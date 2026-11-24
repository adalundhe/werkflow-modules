from __future__ import annotations

from typing import Any
from ..models.api import (
    EntityProperty,
    PropertyKeys,
)
from .base import JiraBaseService


class IssueWorklogPropertiesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue worklog properties (4 operations)."""

    async def delete_worklog_property(
        self,
        issue_id_or_key: str,
        worklog_id: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey} — Delete worklog property"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}',
            path_params={'issueIdOrKey': issue_id_or_key, 'worklogId': worklog_id, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_worklog_property(
        self,
        issue_id_or_key: str,
        worklog_id: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> EntityProperty:
        """GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey} — Get worklog property"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}',
            path_params={'issueIdOrKey': issue_id_or_key, 'worklogId': worklog_id, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, EntityProperty)

    async def get_worklog_property_keys(
        self,
        issue_id_or_key: str,
        worklog_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PropertyKeys:
        """GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties — Get worklog property keys"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties',
            path_params={'issueIdOrKey': issue_id_or_key, 'worklogId': worklog_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PropertyKeys)

    async def set_worklog_property(
        self,
        issue_id_or_key: str,
        worklog_id: str,
        property_key: str,
        body: Any,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey} — Set worklog property"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}',
            path_params={'issueIdOrKey': issue_id_or_key, 'worklogId': worklog_id, 'propertyKey': property_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
