from __future__ import annotations

from typing import Any
from ..models.api import (
    Locale,
    User,
)
from .base import JiraBaseService


class MyselfService(JiraBaseService):
    """Jira Cloud REST API v3 — Myself (6 operations)."""

    async def get_current_user(
        self,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> User:
        """GET /rest/api/3/myself — Get current user"""
        response = await self._request(
            'GET',
            '/rest/api/3/myself',
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, User)

    async def get_locale(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Locale:
        """GET /rest/api/3/mypreferences/locale — Get locale"""
        response = await self._request(
            'GET',
            '/rest/api/3/mypreferences/locale',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Locale)

    async def get_preference(
        self,
        key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> str:
        """GET /rest/api/3/mypreferences — Get preference"""
        response = await self._request(
            'GET',
            '/rest/api/3/mypreferences',
            query_params={'key': key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        payload = self._parse_json(response)
        return str(payload) if payload is not None else ""

    async def remove_preference(
        self,
        key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/mypreferences — Delete preference"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/mypreferences',
            query_params={'key': key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def set_locale(
        self,
        body: Locale | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/mypreferences/locale — Set locale"""
        response = await self._request(
            'PUT',
            '/rest/api/3/mypreferences/locale',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def set_preference(
        self,
        body: str,
        key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/mypreferences — Set preference"""
        response = await self._request(
            'PUT',
            '/rest/api/3/mypreferences',
            query_params={'key': key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
