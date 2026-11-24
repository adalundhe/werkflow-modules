from __future__ import annotations

from ..models.api import (
    ServiceRegistry,
)
from .base import JiraBaseService


class ServiceRegistryService(JiraBaseService):
    """Jira Cloud REST API v3 — Service Registry (1 operations)."""

    async def get_services(
        self,
        service_ids: list[str],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ServiceRegistry]:
        """GET /rest/atlassian-connect/1/service-registry — Retrieve the attributes of service registries"""
        response = await self._request(
            'GET',
            '/rest/atlassian-connect/1/service-registry',
            query_params={'serviceIds': service_ids},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ServiceRegistry)
