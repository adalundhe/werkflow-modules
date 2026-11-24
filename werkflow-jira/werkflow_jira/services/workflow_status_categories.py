from __future__ import annotations

from ..models.api import (
    StatusCategory,
)
from .base import JiraBaseService


class WorkflowStatusCategoriesService(JiraBaseService):
    """Jira Cloud REST API v3 — Workflow status categories (2 operations)."""

    async def get_status_categories(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[StatusCategory]:
        """GET /rest/api/3/statuscategory — Get all status categories"""
        response = await self._request(
            'GET',
            '/rest/api/3/statuscategory',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, StatusCategory)

    async def get_status_category(
        self,
        id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> StatusCategory:
        """GET /rest/api/3/statuscategory/{idOrKey} — Get status category"""
        response = await self._request(
            'GET',
            '/rest/api/3/statuscategory/{idOrKey}',
            path_params={'idOrKey': id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, StatusCategory)
