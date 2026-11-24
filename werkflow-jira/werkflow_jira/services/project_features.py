from __future__ import annotations

from typing import Any
from ..models.api import (
    ContainerForProjectFeatures,
    ProjectFeatureState,
)
from .base import JiraBaseService


class ProjectFeaturesService(JiraBaseService):
    """Jira Cloud REST API v3 — Project features (2 operations)."""

    async def get_features_for_project(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ContainerForProjectFeatures:
        """GET /rest/api/3/project/{projectIdOrKey}/features — Get project features"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/features',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ContainerForProjectFeatures)

    async def toggle_feature_for_project(
        self,
        project_id_or_key: str,
        feature_key: str,
        body: ProjectFeatureState | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ContainerForProjectFeatures:
        """PUT /rest/api/3/project/{projectIdOrKey}/features/{featureKey} — Set project feature state"""
        response = await self._request(
            'PUT',
            '/rest/api/3/project/{projectIdOrKey}/features/{featureKey}',
            path_params={'projectIdOrKey': project_id_or_key, 'featureKey': feature_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ContainerForProjectFeatures)
