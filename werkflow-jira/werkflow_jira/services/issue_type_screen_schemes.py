from __future__ import annotations

from typing import Any
from ..models.api import (
    IssueTypeIds,
    IssueTypeScreenSchemeDetails,
    IssueTypeScreenSchemeId,
    IssueTypeScreenSchemeMappingDetails,
    IssueTypeScreenSchemeProjectAssociation,
    IssueTypeScreenSchemeUpdateDetails,
    PageBeanIssueTypeScreenScheme,
    PageBeanIssueTypeScreenSchemeItem,
    PageBeanIssueTypeScreenSchemesProjects,
    PageBeanProjectDetails,
    UpdateDefaultScreenScheme,
)
from .base import JiraBaseService


class IssueTypeScreenSchemesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue type screen schemes (11 operations)."""

    async def append_mappings_for_issue_type_screen_scheme(
        self,
        issue_type_screen_scheme_id: str,
        body: IssueTypeScreenSchemeMappingDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping — Append mappings to issue type screen scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping',
            path_params={'issueTypeScreenSchemeId': issue_type_screen_scheme_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def assign_issue_type_screen_scheme_to_project(
        self,
        body: IssueTypeScreenSchemeProjectAssociation | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuetypescreenscheme/project — Assign issue type screen scheme to project"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuetypescreenscheme/project',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def create_issue_type_screen_scheme(
        self,
        body: IssueTypeScreenSchemeDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueTypeScreenSchemeId:
        """POST /rest/api/3/issuetypescreenscheme — Create issue type screen scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/issuetypescreenscheme',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueTypeScreenSchemeId)

    async def delete_issue_type_screen_scheme(
        self,
        issue_type_screen_scheme_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId} — Delete issue type screen scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}',
            path_params={'issueTypeScreenSchemeId': issue_type_screen_scheme_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_issue_type_screen_scheme_mappings(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        issue_type_screen_scheme_id: list[int] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueTypeScreenSchemeItem:
        """GET /rest/api/3/issuetypescreenscheme/mapping — Get issue type screen scheme items"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetypescreenscheme/mapping',
            query_params={'startAt': start_at, 'maxResults': max_results, 'issueTypeScreenSchemeId': issue_type_screen_scheme_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueTypeScreenSchemeItem)

    async def get_issue_type_screen_scheme_project_associations(
        self,
        project_id: list[int],
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueTypeScreenSchemesProjects:
        """GET /rest/api/3/issuetypescreenscheme/project — Get issue type screen schemes for projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetypescreenscheme/project',
            query_params={'startAt': start_at, 'maxResults': max_results, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueTypeScreenSchemesProjects)

    async def get_issue_type_screen_schemes(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        id: list[int] | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueTypeScreenScheme:
        """GET /rest/api/3/issuetypescreenscheme — Get issue type screen schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetypescreenscheme',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'queryString': query_string, 'orderBy': order_by, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueTypeScreenScheme)

    async def get_projects_for_issue_type_screen_scheme(
        self,
        issue_type_screen_scheme_id: int,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        query: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanProjectDetails:
        """GET /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project — Get issue type screen scheme projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project',
            path_params={'issueTypeScreenSchemeId': issue_type_screen_scheme_id},
            query_params={'startAt': start_at, 'maxResults': max_results, 'query': query},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanProjectDetails)

    async def remove_mappings_from_issue_type_screen_scheme(
        self,
        issue_type_screen_scheme_id: str,
        body: IssueTypeIds | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove — Remove mappings from issue type screen scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove',
            path_params={'issueTypeScreenSchemeId': issue_type_screen_scheme_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_default_screen_scheme(
        self,
        issue_type_screen_scheme_id: str,
        body: UpdateDefaultScreenScheme | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default — Update issue type screen scheme default screen scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default',
            path_params={'issueTypeScreenSchemeId': issue_type_screen_scheme_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_issue_type_screen_scheme(
        self,
        issue_type_screen_scheme_id: str,
        body: IssueTypeScreenSchemeUpdateDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId} — Update issue type screen scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}',
            path_params={'issueTypeScreenSchemeId': issue_type_screen_scheme_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
