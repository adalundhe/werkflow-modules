from __future__ import annotations

from typing import Any
from ..models.api import (
    JqlFunctionPrecomputationGetByIdRequest,
    JqlFunctionPrecomputationGetByIdResponse,
    JqlFunctionPrecomputationUpdateRequestBean,
    JqlFunctionPrecomputationUpdateResponse,
    PageBean2JqlFunctionPrecomputationBean,
)
from .base import JiraBaseService


class JQLFunctionsAppsService(JiraBaseService):
    """Jira Cloud REST API v3 — JQL functions (apps) (3 operations)."""

    async def get_precomputations(
        self,
        *,
        function_key: list[str] | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBean2JqlFunctionPrecomputationBean:
        """GET /rest/api/3/jql/function/computation — Get precomputations (apps)"""
        response = await self._request(
            'GET',
            '/rest/api/3/jql/function/computation',
            query_params={'functionKey': function_key, 'startAt': start_at, 'maxResults': max_results, 'orderBy': order_by},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBean2JqlFunctionPrecomputationBean)

    async def get_precomputations_by_id(
        self,
        body: JqlFunctionPrecomputationGetByIdRequest | dict[str, Any],
        *,
        order_by: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> JqlFunctionPrecomputationGetByIdResponse:
        """POST /rest/api/3/jql/function/computation/search — Get precomputations by ID (apps)"""
        response = await self._request(
            'POST',
            '/rest/api/3/jql/function/computation/search',
            query_params={'orderBy': order_by},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, JqlFunctionPrecomputationGetByIdResponse)

    async def update_precomputations(
        self,
        body: JqlFunctionPrecomputationUpdateRequestBean | dict[str, Any],
        *,
        skip_not_found_precomputations: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> JqlFunctionPrecomputationUpdateResponse | None:
        """POST /rest/api/3/jql/function/computation — Update precomputations (apps)"""
        response = await self._request(
            'POST',
            '/rest/api/3/jql/function/computation',
            query_params={'skipNotFoundPrecomputations': skip_not_found_precomputations},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_optional_model(response, JqlFunctionPrecomputationUpdateResponse)
