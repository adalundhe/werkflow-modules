from __future__ import annotations

from ..models.api import (
    ErrorCollection,
)
from .base import JiraBaseService


class ProjectKeyAndNameValidationService(JiraBaseService):
    """Jira Cloud REST API v3 — Project key and name validation (3 operations)."""

    async def get_valid_project_key(
        self,
        *,
        key: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> str:
        """GET /rest/api/3/projectvalidate/validProjectKey — Get valid project key"""
        response = await self._request(
            'GET',
            '/rest/api/3/projectvalidate/validProjectKey',
            query_params={'key': key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        payload = self._parse_json(response)
        return str(payload) if payload is not None else ""

    async def get_valid_project_name(
        self,
        name: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> str:
        """GET /rest/api/3/projectvalidate/validProjectName — Get valid project name"""
        response = await self._request(
            'GET',
            '/rest/api/3/projectvalidate/validProjectName',
            query_params={'name': name},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        payload = self._parse_json(response)
        return str(payload) if payload is not None else ""

    async def validate_project_key(
        self,
        *,
        key: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ErrorCollection:
        """GET /rest/api/3/projectvalidate/key — Validate project key"""
        response = await self._request(
            'GET',
            '/rest/api/3/projectvalidate/key',
            query_params={'key': key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ErrorCollection)
