from __future__ import annotations

from typing import Any
from ..models.api import (
    CustomFieldValueUpdateDetails,
    MultipleCustomFieldValuesUpdateDetails,
)
from .base import JiraBaseService


class IssueCustomFieldValuesAppsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue custom field values (apps) (2 operations)."""

    async def update_custom_field_value(
        self,
        field_id_or_key: str,
        body: CustomFieldValueUpdateDetails | dict[str, Any],
        *,
        generate_changelog: bool | None = None,
        generate_app_events: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/app/field/{fieldIdOrKey}/value — Update custom field value"""
        response = await self._request(
            'PUT',
            '/rest/api/3/app/field/{fieldIdOrKey}/value',
            path_params={'fieldIdOrKey': field_id_or_key},
            query_params={'generateChangelog': generate_changelog, 'generateAppEvents': generate_app_events},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_multiple_custom_field_values(
        self,
        body: MultipleCustomFieldValuesUpdateDetails | dict[str, Any],
        *,
        generate_changelog: bool | None = None,
        generate_app_events: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/app/field/value — Update custom fields"""
        response = await self._request(
            'POST',
            '/rest/api/3/app/field/value',
            query_params={'generateChangelog': generate_changelog, 'generateAppEvents': generate_app_events},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
