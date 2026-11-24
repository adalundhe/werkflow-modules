from __future__ import annotations

from typing import Any
from ..models.api import (
    ApplicationProperty,
    Configuration,
    SimpleApplicationPropertyBean,
)
from .base import JiraBaseService


class JiraSettingsService(JiraBaseService):
    """Jira Cloud REST API v3 — Jira settings (4 operations)."""

    async def get_advanced_settings(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ApplicationProperty]:
        """GET /rest/api/3/application-properties/advanced-settings — Get advanced settings"""
        response = await self._request(
            'GET',
            '/rest/api/3/application-properties/advanced-settings',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ApplicationProperty)

    async def get_application_property(
        self,
        *,
        key: str | None = None,
        permission_level: str | None = None,
        key_filter: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ApplicationProperty]:
        """GET /rest/api/3/application-properties — Get application property"""
        response = await self._request(
            'GET',
            '/rest/api/3/application-properties',
            query_params={'key': key, 'permissionLevel': permission_level, 'keyFilter': key_filter},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ApplicationProperty)

    async def get_configuration(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Configuration:
        """GET /rest/api/3/configuration — Get global settings"""
        response = await self._request(
            'GET',
            '/rest/api/3/configuration',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Configuration)

    async def set_application_property(
        self,
        id: str,
        body: SimpleApplicationPropertyBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ApplicationProperty:
        """PUT /rest/api/3/application-properties/{id} — Set application property"""
        response = await self._request(
            'PUT',
            '/rest/api/3/application-properties/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ApplicationProperty)
