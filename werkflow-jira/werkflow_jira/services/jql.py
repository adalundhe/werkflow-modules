from __future__ import annotations

from typing import Any
from ..models.api import (
    AuditPage,
    AutoCompleteSuggestions,
    ConvertedJQLQueries,
    JQLPersonalDataMigrationRequest,
    JQLReferenceData,
    JqlQueriesToParse,
    JqlQueriesToSanitize,
    ParsedJqlQueries,
    SanitizedJqlQueries,
    SearchAutoCompleteFilter,
)
from .base import JiraBaseService


class JQLService(JiraBaseService):
    """Jira Cloud REST API v3 — JQL (7 operations)."""

    async def get_audit_entries(
        self,
        *,
        user_account_id: str | None = None,
        next_page_token: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> AuditPage:
        """GET /rest/api/3/invalid-jqls-access-log — Get invalid JQL searches"""
        response = await self._request(
            'GET',
            '/rest/api/3/invalid-jqls-access-log',
            query_params={'userAccountId': user_account_id, 'nextPageToken': next_page_token, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, AuditPage)

    async def get_auto_complete(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> JQLReferenceData:
        """GET /rest/api/3/jql/autocompletedata — Get field reference data (GET)"""
        response = await self._request(
            'GET',
            '/rest/api/3/jql/autocompletedata',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, JQLReferenceData)

    async def get_auto_complete_post(
        self,
        body: SearchAutoCompleteFilter | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> JQLReferenceData:
        """POST /rest/api/3/jql/autocompletedata — Get field reference data (POST)"""
        response = await self._request(
            'POST',
            '/rest/api/3/jql/autocompletedata',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, JQLReferenceData)

    async def get_field_auto_complete_for_query_string(
        self,
        *,
        field_name: str | None = None,
        field_value: str | None = None,
        predicate_name: str | None = None,
        predicate_value: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> AutoCompleteSuggestions:
        """GET /rest/api/3/jql/autocompletedata/suggestions — Get field auto complete suggestions"""
        response = await self._request(
            'GET',
            '/rest/api/3/jql/autocompletedata/suggestions',
            query_params={'fieldName': field_name, 'fieldValue': field_value, 'predicateName': predicate_name, 'predicateValue': predicate_value, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, AutoCompleteSuggestions)

    async def migrate_queries(
        self,
        body: JQLPersonalDataMigrationRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ConvertedJQLQueries:
        """POST /rest/api/3/jql/pdcleaner — Convert user identifiers to account IDs in JQL queries"""
        response = await self._request(
            'POST',
            '/rest/api/3/jql/pdcleaner',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ConvertedJQLQueries)

    async def parse_jql_queries(
        self,
        body: JqlQueriesToParse | dict[str, Any],
        validation: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ParsedJqlQueries:
        """POST /rest/api/3/jql/parse — Parse JQL query"""
        response = await self._request(
            'POST',
            '/rest/api/3/jql/parse',
            query_params={'validation': validation},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ParsedJqlQueries)

    async def sanitise_jql_queries(
        self,
        body: JqlQueriesToSanitize | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SanitizedJqlQueries:
        """POST /rest/api/3/jql/sanitize — Sanitize JQL queries"""
        response = await self._request(
            'POST',
            '/rest/api/3/jql/sanitize',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SanitizedJqlQueries)
