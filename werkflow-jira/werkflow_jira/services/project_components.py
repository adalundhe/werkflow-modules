from __future__ import annotations

from typing import Any
from ..models.api import (
    ComponentIssuesCount,
    PageBean2ComponentJsonBean,
    PageBeanComponentWithIssueCount,
    ProjectComponent,
)
from .base import JiraBaseService


class ProjectComponentsService(JiraBaseService):
    """Jira Cloud REST API v3 — Project components (8 operations)."""

    async def create_component(
        self,
        body: ProjectComponent | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectComponent:
        """POST /rest/api/3/component — Create component"""
        response = await self._request(
            'POST',
            '/rest/api/3/component',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectComponent)

    async def delete_component(
        self,
        id: str,
        *,
        move_issues_to: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/component/{id} — Delete component"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/component/{id}',
            path_params={'id': id},
            query_params={'moveIssuesTo': move_issues_to},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def find_components_for_projects(
        self,
        *,
        project_ids_or_keys: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        query: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBean2ComponentJsonBean:
        """GET /rest/api/3/component — Find components for projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/component',
            query_params={'projectIdsOrKeys': project_ids_or_keys, 'startAt': start_at, 'maxResults': max_results, 'orderBy': order_by, 'query': query},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBean2ComponentJsonBean)

    async def get_component(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectComponent:
        """GET /rest/api/3/component/{id} — Get component"""
        response = await self._request(
            'GET',
            '/rest/api/3/component/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectComponent)

    async def get_component_related_issues(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ComponentIssuesCount:
        """GET /rest/api/3/component/{id}/relatedIssueCounts — Get component issues count"""
        response = await self._request(
            'GET',
            '/rest/api/3/component/{id}/relatedIssueCounts',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ComponentIssuesCount)

    async def get_project_components(
        self,
        project_id_or_key: str,
        *,
        component_source: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ProjectComponent]:
        """GET /rest/api/3/project/{projectIdOrKey}/components — Get project components"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/components',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'componentSource': component_source},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ProjectComponent)

    async def get_project_components_paginated(
        self,
        project_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        component_source: str | None = None,
        query: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanComponentWithIssueCount:
        """GET /rest/api/3/project/{projectIdOrKey}/component — Get project components paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/component',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'startAt': start_at, 'maxResults': max_results, 'orderBy': order_by, 'componentSource': component_source, 'query': query},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanComponentWithIssueCount)

    async def update_component(
        self,
        id: str,
        body: ProjectComponent | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectComponent:
        """PUT /rest/api/3/component/{id} — Update component"""
        response = await self._request(
            'PUT',
            '/rest/api/3/component/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectComponent)
