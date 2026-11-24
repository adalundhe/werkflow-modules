from __future__ import annotations

from typing import Any
from ..models.api import (
    IssueTypeIds,
    IssueTypeSchemeDetails,
    IssueTypeSchemeID,
    IssueTypeSchemeProjectAssociation,
    IssueTypeSchemeUpdateDetails,
    OrderOfIssueTypes,
    PageBeanIssueTypeScheme,
    PageBeanIssueTypeSchemeMapping,
    PageBeanIssueTypeSchemeProjects,
)
from .base import JiraBaseService


class IssueTypeSchemesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue type schemes (10 operations)."""

    async def add_issue_types_to_issue_type_scheme(
        self,
        issue_type_scheme_id: int,
        body: IssueTypeIds | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype — Add issue types to issue type scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype',
            path_params={'issueTypeSchemeId': issue_type_scheme_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def assign_issue_type_scheme_to_project(
        self,
        body: IssueTypeSchemeProjectAssociation | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuetypescheme/project — Assign issue type scheme to project"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuetypescheme/project',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def create_issue_type_scheme(
        self,
        body: IssueTypeSchemeDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueTypeSchemeID:
        """POST /rest/api/3/issuetypescheme — Create issue type scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/issuetypescheme',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueTypeSchemeID)

    async def delete_issue_type_scheme(
        self,
        issue_type_scheme_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId} — Delete issue type scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issuetypescheme/{issueTypeSchemeId}',
            path_params={'issueTypeSchemeId': issue_type_scheme_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_all_issue_type_schemes(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id: list[int] | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueTypeScheme:
        """GET /rest/api/3/issuetypescheme — Get all issue type schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetypescheme',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'orderBy': order_by, 'expand': expand, 'queryString': query_string},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueTypeScheme)

    async def get_issue_type_scheme_for_projects(
        self,
        project_id: list[int],
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueTypeSchemeProjects:
        """GET /rest/api/3/issuetypescheme/project — Get issue type schemes for projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetypescheme/project',
            query_params={'startAt': start_at, 'maxResults': max_results, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueTypeSchemeProjects)

    async def get_issue_type_schemes_mapping(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_type_scheme_id: list[int] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueTypeSchemeMapping:
        """GET /rest/api/3/issuetypescheme/mapping — Get issue type scheme items"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetypescheme/mapping',
            query_params={'startAt': start_at, 'maxResults': max_results, 'issueTypeSchemeId': issue_type_scheme_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueTypeSchemeMapping)

    async def remove_issue_type_from_issue_type_scheme(
        self,
        issue_type_scheme_id: int,
        issue_type_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId} — Remove issue type from issue type scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}',
            path_params={'issueTypeSchemeId': issue_type_scheme_id, 'issueTypeId': issue_type_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def reorder_issue_types_in_issue_type_scheme(
        self,
        issue_type_scheme_id: int,
        body: OrderOfIssueTypes | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move — Change order of issue types"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move',
            path_params={'issueTypeSchemeId': issue_type_scheme_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_issue_type_scheme(
        self,
        issue_type_scheme_id: int,
        body: IssueTypeSchemeUpdateDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId} — Update issue type scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuetypescheme/{issueTypeSchemeId}',
            path_params={'issueTypeSchemeId': issue_type_scheme_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
