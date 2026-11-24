from __future__ import annotations

from typing import Any
from ..models.api import (
    CreatePrioritySchemeDetails,
    PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects,
    PageBeanPriorityWithSequence,
    PageBeanProject,
    PrioritySchemeId,
    SuggestedMappingsRequestBean,
    UpdatePrioritySchemeRequestBean,
    UpdatePrioritySchemeResponseBean,
)
from .base import JiraBaseService


class PrioritySchemesService(JiraBaseService):
    """Jira Cloud REST API v3 — Priority schemes (8 operations)."""

    async def create_priority_scheme(
        self,
        body: CreatePrioritySchemeDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PrioritySchemeId:
        """POST /rest/api/3/priorityscheme — Create priority scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/priorityscheme',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PrioritySchemeId)

    async def delete_priority_scheme(
        self,
        scheme_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/priorityscheme/{schemeId} — Delete priority scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/priorityscheme/{schemeId}',
            path_params={'schemeId': scheme_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_available_priorities_by_priority_scheme(
        self,
        scheme_id: str,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        query: str | None = None,
        exclude: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanPriorityWithSequence:
        """GET /rest/api/3/priorityscheme/priorities/available — Get available priorities by priority scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/priorityscheme/priorities/available',
            query_params={'startAt': start_at, 'maxResults': max_results, 'query': query, 'schemeId': scheme_id, 'exclude': exclude},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanPriorityWithSequence)

    async def get_priorities_by_priority_scheme(
        self,
        scheme_id: str,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanPriorityWithSequence:
        """GET /rest/api/3/priorityscheme/{schemeId}/priorities — Get priorities by priority scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/priorityscheme/{schemeId}/priorities',
            path_params={'schemeId': scheme_id},
            query_params={'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanPriorityWithSequence)

    async def get_priority_schemes(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        priority_id: list[int] | None = None,
        scheme_id: list[int] | None = None,
        scheme_name: str | None = None,
        only_default: bool | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects:
        """GET /rest/api/3/priorityscheme — Get priority schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/priorityscheme',
            query_params={'startAt': start_at, 'maxResults': max_results, 'priorityId': priority_id, 'schemeId': scheme_id, 'schemeName': scheme_name, 'onlyDefault': only_default, 'orderBy': order_by, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects)

    async def get_projects_by_priority_scheme(
        self,
        scheme_id: str,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        project_id: list[int] | None = None,
        query: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanProject:
        """GET /rest/api/3/priorityscheme/{schemeId}/projects — Get projects by priority scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/priorityscheme/{schemeId}/projects',
            path_params={'schemeId': scheme_id},
            query_params={'startAt': start_at, 'maxResults': max_results, 'projectId': project_id, 'query': query},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanProject)

    async def suggested_priorities_for_mappings(
        self,
        body: SuggestedMappingsRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanPriorityWithSequence:
        """POST /rest/api/3/priorityscheme/mappings — Suggested priorities for mappings"""
        response = await self._request(
            'POST',
            '/rest/api/3/priorityscheme/mappings',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanPriorityWithSequence)

    async def update_priority_scheme(
        self,
        scheme_id: int,
        body: UpdatePrioritySchemeRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> UpdatePrioritySchemeResponseBean:
        """PUT /rest/api/3/priorityscheme/{schemeId} — Update priority scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/priorityscheme/{schemeId}',
            path_params={'schemeId': scheme_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, UpdatePrioritySchemeResponseBean)
