from __future__ import annotations

from typing import Any
from ..models.api import (
    BulkIssuePropertyUpdateRequest,
    EntityProperty,
    IssueEntityProperties,
    IssueFilterForBulkPropertyDelete,
    MultiIssueEntityProperties,
    PropertyKeys,
)
from .base import JiraBaseService


class IssuePropertiesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue properties (8 operations)."""

    async def bulk_delete_issue_property(
        self,
        property_key: str,
        body: IssueFilterForBulkPropertyDelete | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/properties/{propertyKey} — Bulk delete issue property"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/properties/{propertyKey}',
            path_params={'propertyKey': property_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def bulk_set_issue_properties_by_issue(
        self,
        body: MultiIssueEntityProperties | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """POST /rest/api/3/issue/properties/multi — Bulk set issue properties by issue"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/properties/multi',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def bulk_set_issue_property(
        self,
        property_key: str,
        body: BulkIssuePropertyUpdateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """PUT /rest/api/3/issue/properties/{propertyKey} — Bulk set issue property"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issue/properties/{propertyKey}',
            path_params={'propertyKey': property_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def bulk_set_issues_properties_list(
        self,
        body: IssueEntityProperties | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """POST /rest/api/3/issue/properties — Bulk set issues properties by list"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/properties',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_issue_property(
        self,
        issue_id_or_key: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey} — Delete issue property"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}',
            path_params={'issueIdOrKey': issue_id_or_key, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_issue_property(
        self,
        issue_id_or_key: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> EntityProperty:
        """GET /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey} — Get issue property"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}',
            path_params={'issueIdOrKey': issue_id_or_key, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, EntityProperty)

    async def get_issue_property_keys(
        self,
        issue_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PropertyKeys:
        """GET /rest/api/3/issue/{issueIdOrKey}/properties — Get issue property keys"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/properties',
            path_params={'issueIdOrKey': issue_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PropertyKeys)

    async def set_issue_property(
        self,
        issue_id_or_key: str,
        property_key: str,
        body: Any,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey} — Set issue property"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}',
            path_params={'issueIdOrKey': issue_id_or_key, 'propertyKey': property_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
