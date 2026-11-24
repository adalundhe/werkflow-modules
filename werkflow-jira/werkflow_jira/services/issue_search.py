from __future__ import annotations

from typing import Any
from ..models.api import (
    IssueMatches,
    IssuePickerSuggestions,
    IssuesAndJQLQueries,
    JQLCountRequestBean,
    JQLCountResultsBean,
    SearchAndReconcileRequestBean,
    SearchAndReconcileResults,
    SearchRequestBean,
    SearchResults,
)
from .base import JiraBaseService


class IssueSearchService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue search (7 operations)."""

    async def count_issues(
        self,
        body: JQLCountRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> JQLCountResultsBean:
        """POST /rest/api/3/search/approximate-count — Count issues using JQL"""
        response = await self._request(
            'POST',
            '/rest/api/3/search/approximate-count',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, JQLCountResultsBean)

    async def get_issue_picker_resource(
        self,
        *,
        query: str | None = None,
        current_jql: str | None = None,
        current_issue_key: str | None = None,
        current_project_id: str | None = None,
        show_sub_tasks: bool | None = None,
        show_sub_task_parent: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssuePickerSuggestions:
        """GET /rest/api/3/issue/picker — Get issue picker suggestions"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/picker',
            query_params={'query': query, 'currentJQL': current_jql, 'currentIssueKey': current_issue_key, 'currentProjectId': current_project_id, 'showSubTasks': show_sub_tasks, 'showSubTaskParent': show_sub_task_parent},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssuePickerSuggestions)

    async def match_issues(
        self,
        body: IssuesAndJQLQueries | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueMatches:
        """POST /rest/api/3/jql/match — Check issues against JQL"""
        response = await self._request(
            'POST',
            '/rest/api/3/jql/match',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueMatches)

    async def search_and_reconsile_issues_using_jql(
        self,
        *,
        jql: str | None = None,
        next_page_token: str | None = None,
        max_results: int | None = None,
        fields: list[str] | None = None,
        expand: str | None = None,
        properties: list[str] | None = None,
        fields_by_keys: bool | None = None,
        fail_fast: bool | None = None,
        reconcile_issues: list[int] | None = None,
        include_archived_projects: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SearchAndReconcileResults:
        """GET /rest/api/3/search/jql — Search for issues using JQL enhanced search (GET)"""
        response = await self._request(
            'GET',
            '/rest/api/3/search/jql',
            query_params={'jql': jql, 'nextPageToken': next_page_token, 'maxResults': max_results, 'fields': fields, 'expand': expand, 'properties': properties, 'fieldsByKeys': fields_by_keys, 'failFast': fail_fast, 'reconcileIssues': reconcile_issues, 'includeArchivedProjects': include_archived_projects},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SearchAndReconcileResults)

    async def search_and_reconsile_issues_using_jql_post(
        self,
        body: SearchAndReconcileRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SearchAndReconcileResults:
        """POST /rest/api/3/search/jql — Search for issues using JQL enhanced search (POST)"""
        response = await self._request(
            'POST',
            '/rest/api/3/search/jql',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SearchAndReconcileResults)

    async def search_for_issues_using_jql(
        self,
        *,
        jql: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        validate_query: str | None = None,
        fields: list[str] | None = None,
        expand: str | None = None,
        properties: list[str] | None = None,
        fields_by_keys: bool | None = None,
        fail_fast: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SearchResults:
        """GET /rest/api/3/search — Currently being removed. Search for issues using JQL (GET)"""
        response = await self._request(
            'GET',
            '/rest/api/3/search',
            query_params={'jql': jql, 'startAt': start_at, 'maxResults': max_results, 'validateQuery': validate_query, 'fields': fields, 'expand': expand, 'properties': properties, 'fieldsByKeys': fields_by_keys, 'failFast': fail_fast},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SearchResults)

    async def search_for_issues_using_jql_post(
        self,
        body: SearchRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SearchResults:
        """POST /rest/api/3/search — Currently being removed. Search for issues using JQL (POST)"""
        response = await self._request(
            'POST',
            '/rest/api/3/search',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SearchResults)
