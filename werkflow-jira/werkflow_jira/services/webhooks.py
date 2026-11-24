from __future__ import annotations

from typing import Any
from ..models.api import (
    ContainerForRegisteredWebhooks,
    ContainerForWebhookIDs,
    FailedWebhooks,
    PageBeanWebhook,
    WebhookRegistrationDetails,
    WebhooksExpirationDate,
)
from .base import JiraBaseService


class WebhooksService(JiraBaseService):
    """Jira Cloud REST API v3 — Webhooks (5 operations)."""

    async def delete_webhook_by_id(
        self,
        body: ContainerForWebhookIDs | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/webhook — Delete webhooks by ID"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/webhook',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_dynamic_webhooks_for_app(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanWebhook:
        """GET /rest/api/3/webhook — Get dynamic webhooks for app"""
        response = await self._request(
            'GET',
            '/rest/api/3/webhook',
            query_params={'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanWebhook)

    async def get_failed_webhooks(
        self,
        *,
        max_results: int | None = None,
        after: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> FailedWebhooks:
        """GET /rest/api/3/webhook/failed — Get failed webhooks"""
        response = await self._request(
            'GET',
            '/rest/api/3/webhook/failed',
            query_params={'maxResults': max_results, 'after': after},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, FailedWebhooks)

    async def refresh_webhooks(
        self,
        body: ContainerForWebhookIDs | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WebhooksExpirationDate:
        """PUT /rest/api/3/webhook/refresh — Extend webhook life"""
        response = await self._request(
            'PUT',
            '/rest/api/3/webhook/refresh',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WebhooksExpirationDate)

    async def register_dynamic_webhooks(
        self,
        body: WebhookRegistrationDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ContainerForRegisteredWebhooks:
        """POST /rest/api/3/webhook — Register dynamic webhooks"""
        response = await self._request(
            'POST',
            '/rest/api/3/webhook',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ContainerForRegisteredWebhooks)
