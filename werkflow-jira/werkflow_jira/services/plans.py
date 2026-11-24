from __future__ import annotations

from typing import Any
from ..models.api import (
    CreatePlanRequest,
    DuplicatePlanRequest,
    GetPlanResponse,
    PageWithCursorGetPlanResponseForPage,
)
from .base import JiraBaseService


class PlansService(JiraBaseService):
    """Jira Cloud REST API v3 — Plans (7 operations)."""

    async def archive_plan(
        self,
        plan_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/plans/plan/{planId}/archive — Archive plan"""
        response = await self._request(
            'PUT',
            '/rest/api/3/plans/plan/{planId}/archive',
            path_params={'planId': plan_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def create_plan(
        self,
        body: CreatePlanRequest | dict[str, Any],
        *,
        use_group_id: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> int:
        """POST /rest/api/3/plans/plan — Create plan"""
        response = await self._request(
            'POST',
            '/rest/api/3/plans/plan',
            query_params={'useGroupId': use_group_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        payload = self._parse_json(response)
        return int(payload) if payload is not None else 0

    async def duplicate_plan(
        self,
        plan_id: int,
        body: DuplicatePlanRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> int:
        """POST /rest/api/3/plans/plan/{planId}/duplicate — Duplicate plan"""
        response = await self._request(
            'POST',
            '/rest/api/3/plans/plan/{planId}/duplicate',
            path_params={'planId': plan_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        payload = self._parse_json(response)
        return int(payload) if payload is not None else 0

    async def get_plan(
        self,
        plan_id: int,
        *,
        use_group_id: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> GetPlanResponse:
        """GET /rest/api/3/plans/plan/{planId} — Get plan"""
        response = await self._request(
            'GET',
            '/rest/api/3/plans/plan/{planId}',
            path_params={'planId': plan_id},
            query_params={'useGroupId': use_group_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, GetPlanResponse)

    async def get_plans(
        self,
        *,
        include_trashed: bool | None = None,
        include_archived: bool | None = None,
        cursor: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageWithCursorGetPlanResponseForPage:
        """GET /rest/api/3/plans/plan — Get plans paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/plans/plan',
            query_params={'includeTrashed': include_trashed, 'includeArchived': include_archived, 'cursor': cursor, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageWithCursorGetPlanResponseForPage)

    async def trash_plan(
        self,
        plan_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/plans/plan/{planId}/trash — Trash plan"""
        response = await self._request(
            'PUT',
            '/rest/api/3/plans/plan/{planId}/trash',
            path_params={'planId': plan_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_plan(
        self,
        plan_id: int,
        body: list[dict[str, Any]] | dict[str, Any],
        *,
        use_group_id: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/plans/plan/{planId} — Update plan"""
        response = await self._request(
            'PUT',
            '/rest/api/3/plans/plan/{planId}',
            path_params={'planId': plan_id},
            query_params={'useGroupId': use_group_id},
            body=body,
            content_type='application/json-patch+json',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
