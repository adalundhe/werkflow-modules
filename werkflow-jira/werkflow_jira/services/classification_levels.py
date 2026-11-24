from __future__ import annotations

from ..models.api import (
    DataClassificationLevelsBean,
)
from .base import JiraBaseService


class ClassificationLevelsService(JiraBaseService):
    """Jira Cloud REST API v3 — Classification levels (1 operations)."""

    async def get_all_user_data_classification_levels(
        self,
        *,
        status: list[str] | None = None,
        order_by: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> DataClassificationLevelsBean:
        """GET /rest/api/3/classification-levels — Get all classification levels"""
        response = await self._request(
            'GET',
            '/rest/api/3/classification-levels',
            query_params={'status': status, 'orderBy': order_by},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, DataClassificationLevelsBean)
