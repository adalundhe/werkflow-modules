from __future__ import annotations

from typing import Any
from ..models.api import (
    IssueFieldOption,
    IssueFieldOptionCreateBean,
    PageBeanIssueFieldOption,
)
from .base import JiraBaseService


class IssueCustomFieldOptionsAppsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue custom field options (apps) (8 operations)."""

    async def create_issue_field_option(
        self,
        field_key: str,
        body: IssueFieldOptionCreateBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueFieldOption:
        """POST /rest/api/3/field/{fieldKey}/option — Create issue field option"""
        response = await self._request(
            'POST',
            '/rest/api/3/field/{fieldKey}/option',
            path_params={'fieldKey': field_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueFieldOption)

    async def delete_issue_field_option(
        self,
        field_key: str,
        option_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/field/{fieldKey}/option/{optionId} — Delete issue field option"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/field/{fieldKey}/option/{optionId}',
            path_params={'fieldKey': field_key, 'optionId': option_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_all_issue_field_options(
        self,
        field_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueFieldOption:
        """GET /rest/api/3/field/{fieldKey}/option — Get all issue field options"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldKey}/option',
            path_params={'fieldKey': field_key},
            query_params={'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueFieldOption)

    async def get_issue_field_option(
        self,
        field_key: str,
        option_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueFieldOption:
        """GET /rest/api/3/field/{fieldKey}/option/{optionId} — Get issue field option"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldKey}/option/{optionId}',
            path_params={'fieldKey': field_key, 'optionId': option_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueFieldOption)

    async def get_selectable_issue_field_options(
        self,
        field_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueFieldOption:
        """GET /rest/api/3/field/{fieldKey}/option/suggestions/edit — Get selectable issue field options"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldKey}/option/suggestions/edit',
            path_params={'fieldKey': field_key},
            query_params={'startAt': start_at, 'maxResults': max_results, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueFieldOption)

    async def get_visible_issue_field_options(
        self,
        field_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        project_id: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueFieldOption:
        """GET /rest/api/3/field/{fieldKey}/option/suggestions/search — Get visible issue field options"""
        response = await self._request(
            'GET',
            '/rest/api/3/field/{fieldKey}/option/suggestions/search',
            path_params={'fieldKey': field_key},
            query_params={'startAt': start_at, 'maxResults': max_results, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueFieldOption)

    async def replace_issue_field_option(
        self,
        field_key: str,
        option_id: int,
        *,
        replace_with: int | None = None,
        jql: str | None = None,
        override_screen_security: bool | None = None,
        override_editable_flag: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/field/{fieldKey}/option/{optionId}/issue — Replace issue field option"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/field/{fieldKey}/option/{optionId}/issue',
            path_params={'fieldKey': field_key, 'optionId': option_id},
            query_params={'replaceWith': replace_with, 'jql': jql, 'overrideScreenSecurity': override_screen_security, 'overrideEditableFlag': override_editable_flag},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def update_issue_field_option(
        self,
        field_key: str,
        option_id: int,
        body: IssueFieldOption | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueFieldOption:
        """PUT /rest/api/3/field/{fieldKey}/option/{optionId} — Update issue field option"""
        response = await self._request(
            'PUT',
            '/rest/api/3/field/{fieldKey}/option/{optionId}',
            path_params={'fieldKey': field_key, 'optionId': option_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueFieldOption)
