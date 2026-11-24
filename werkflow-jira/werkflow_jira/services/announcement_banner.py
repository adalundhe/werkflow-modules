from __future__ import annotations

from typing import Any
from ..models.api import (
    AnnouncementBannerConfiguration,
    AnnouncementBannerConfigurationUpdate,
)
from .base import JiraBaseService


class AnnouncementBannerService(JiraBaseService):
    """Jira Cloud REST API v3 — Announcement banner (2 operations)."""

    async def get_banner(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> AnnouncementBannerConfiguration:
        """GET /rest/api/3/announcementBanner — Get announcement banner configuration"""
        response = await self._request(
            'GET',
            '/rest/api/3/announcementBanner',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, AnnouncementBannerConfiguration)

    async def set_banner(
        self,
        body: AnnouncementBannerConfigurationUpdate | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/announcementBanner — Update announcement banner configuration"""
        response = await self._request(
            'PUT',
            '/rest/api/3/announcementBanner',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
