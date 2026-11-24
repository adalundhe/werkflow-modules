from __future__ import annotations

from typing import Any
from ..models.api import (
    ConnectModules,
)
from .base import JiraBaseService


class DynamicModulesService(JiraBaseService):
    """Jira Cloud REST API v3 — Dynamic modules (3 operations)."""

    async def get_modules(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ConnectModules:
        """GET /rest/atlassian-connect/1/app/module/dynamic — Get modules"""
        response = await self._request(
            'GET',
            '/rest/atlassian-connect/1/app/module/dynamic',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ConnectModules)

    async def register_modules(
        self,
        body: ConnectModules | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """POST /rest/atlassian-connect/1/app/module/dynamic — Register modules"""
        response = await self._request(
            'POST',
            '/rest/atlassian-connect/1/app/module/dynamic',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def remove_modules(
        self,
        *,
        module_key: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/atlassian-connect/1/app/module/dynamic — Remove modules"""
        response = await self._request(
            'DELETE',
            '/rest/atlassian-connect/1/app/module/dynamic',
            query_params={'moduleKey': module_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None
