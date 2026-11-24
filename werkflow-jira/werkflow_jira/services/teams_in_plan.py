from __future__ import annotations

from typing import Any
from ..models.api import (
    AddAtlassianTeamRequest,
    CreatePlanOnlyTeamRequest,
    GetAtlassianTeamResponse,
    GetPlanOnlyTeamResponse,
    PageWithCursorGetTeamResponseForPage,
)
from .base import JiraBaseService


class TeamsInPlanService(JiraBaseService):
    """Jira Cloud REST API v3 — Teams in plan (9 operations)."""

    async def add_atlassian_team(
        self,
        plan_id: int,
        body: AddAtlassianTeamRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/plans/plan/{planId}/team/atlassian — Add Atlassian team to plan"""
        response = await self._request(
            'POST',
            '/rest/api/3/plans/plan/{planId}/team/atlassian',
            path_params={'planId': plan_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def create_plan_only_team(
        self,
        plan_id: int,
        body: CreatePlanOnlyTeamRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> int:
        """POST /rest/api/3/plans/plan/{planId}/team/planonly — Create plan-only team"""
        response = await self._request(
            'POST',
            '/rest/api/3/plans/plan/{planId}/team/planonly',
            path_params={'planId': plan_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        payload = self._parse_json(response)
        return int(payload) if payload is not None else 0

    async def delete_plan_only_team(
        self,
        plan_id: int,
        plan_only_team_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId} — Delete plan-only team"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}',
            path_params={'planId': plan_id, 'planOnlyTeamId': plan_only_team_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_atlassian_team(
        self,
        plan_id: int,
        atlassian_team_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> GetAtlassianTeamResponse:
        """GET /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId} — Get Atlassian team in plan"""
        response = await self._request(
            'GET',
            '/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}',
            path_params={'planId': plan_id, 'atlassianTeamId': atlassian_team_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, GetAtlassianTeamResponse)

    async def get_plan_only_team(
        self,
        plan_id: int,
        plan_only_team_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> GetPlanOnlyTeamResponse:
        """GET /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId} — Get plan-only team"""
        response = await self._request(
            'GET',
            '/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}',
            path_params={'planId': plan_id, 'planOnlyTeamId': plan_only_team_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, GetPlanOnlyTeamResponse)

    async def get_teams(
        self,
        plan_id: int,
        *,
        cursor: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageWithCursorGetTeamResponseForPage:
        """GET /rest/api/3/plans/plan/{planId}/team — Get teams in plan paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/plans/plan/{planId}/team',
            path_params={'planId': plan_id},
            query_params={'cursor': cursor, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageWithCursorGetTeamResponseForPage)

    async def remove_atlassian_team(
        self,
        plan_id: int,
        atlassian_team_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId} — Remove Atlassian team from plan"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}',
            path_params={'planId': plan_id, 'atlassianTeamId': atlassian_team_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_atlassian_team(
        self,
        plan_id: int,
        atlassian_team_id: str,
        body: list[dict[str, Any]] | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId} — Update Atlassian team in plan"""
        response = await self._request(
            'PUT',
            '/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}',
            path_params={'planId': plan_id, 'atlassianTeamId': atlassian_team_id},
            body=body,
            content_type='application/json-patch+json',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_plan_only_team(
        self,
        plan_id: int,
        plan_only_team_id: int,
        body: list[dict[str, Any]] | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId} — Update plan-only team"""
        response = await self._request(
            'PUT',
            '/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}',
            path_params={'planId': plan_id, 'planOnlyTeamId': plan_only_team_id},
            body=body,
            content_type='application/json-patch+json',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
