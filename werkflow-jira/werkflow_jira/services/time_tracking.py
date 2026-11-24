from __future__ import annotations

from typing import Any
from ..models.api import (
    TimeTrackingConfiguration,
    TimeTrackingProvider,
)
from .base import JiraBaseService


class TimeTrackingService(JiraBaseService):
    """Jira Cloud REST API v3 — Time tracking (5 operations)."""

    async def get_available_time_tracking_implementations(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[TimeTrackingProvider]:
        """GET /rest/api/3/configuration/timetracking/list — Get all time tracking providers"""
        response = await self._request(
            'GET',
            '/rest/api/3/configuration/timetracking/list',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, TimeTrackingProvider)

    async def get_selected_time_tracking_implementation(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> TimeTrackingProvider | None:
        """GET /rest/api/3/configuration/timetracking — Get selected time tracking provider"""
        response = await self._request(
            'GET',
            '/rest/api/3/configuration/timetracking',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_optional_model(response, TimeTrackingProvider)

    async def get_shared_time_tracking_configuration(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> TimeTrackingConfiguration:
        """GET /rest/api/3/configuration/timetracking/options — Get time tracking settings"""
        response = await self._request(
            'GET',
            '/rest/api/3/configuration/timetracking/options',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, TimeTrackingConfiguration)

    async def select_time_tracking_implementation(
        self,
        body: TimeTrackingProvider | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/configuration/timetracking — Select time tracking provider"""
        response = await self._request(
            'PUT',
            '/rest/api/3/configuration/timetracking',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def set_shared_time_tracking_configuration(
        self,
        body: TimeTrackingConfiguration | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> TimeTrackingConfiguration:
        """PUT /rest/api/3/configuration/timetracking/options — Set time tracking settings"""
        response = await self._request(
            'PUT',
            '/rest/api/3/configuration/timetracking/options',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, TimeTrackingConfiguration)
