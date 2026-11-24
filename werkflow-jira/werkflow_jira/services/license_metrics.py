from __future__ import annotations

from ..models.api import (
    License,
    LicenseMetric,
)
from .base import JiraBaseService


class LicenseMetricsService(JiraBaseService):
    """Jira Cloud REST API v3 — License metrics (3 operations)."""

    async def get_approximate_application_license_count(
        self,
        application_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> LicenseMetric:
        """GET /rest/api/3/license/approximateLicenseCount/product/{applicationKey} — Get approximate application license count"""
        response = await self._request(
            'GET',
            '/rest/api/3/license/approximateLicenseCount/product/{applicationKey}',
            path_params={'applicationKey': application_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, LicenseMetric)

    async def get_approximate_license_count(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> LicenseMetric:
        """GET /rest/api/3/license/approximateLicenseCount — Get approximate license count"""
        response = await self._request(
            'GET',
            '/rest/api/3/license/approximateLicenseCount',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, LicenseMetric)

    async def get_license(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> License:
        """GET /rest/api/3/instance/license — Get license"""
        response = await self._request(
            'GET',
            '/rest/api/3/instance/license',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, License)
