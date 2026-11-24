from __future__ import annotations

from typing import Any
from ..models.api import (
    AddNotificationsDetails,
    CreateNotificationSchemeDetails,
    NotificationScheme,
    NotificationSchemeId,
    PageBeanNotificationScheme,
    PageBeanNotificationSchemeAndProjectMappingJsonBean,
    UpdateNotificationSchemeDetails,
)
from .base import JiraBaseService


class IssueNotificationSchemesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue notification schemes (8 operations)."""

    async def add_notifications(
        self,
        id: str,
        body: AddNotificationsDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/notificationscheme/{id}/notification — Add notifications to notification scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/notificationscheme/{id}/notification',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def create_notification_scheme(
        self,
        body: CreateNotificationSchemeDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> NotificationSchemeId:
        """POST /rest/api/3/notificationscheme — Create notification scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/notificationscheme',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, NotificationSchemeId)

    async def delete_notification_scheme(
        self,
        notification_scheme_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/notificationscheme/{notificationSchemeId} — Delete notification scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/notificationscheme/{notificationSchemeId}',
            path_params={'notificationSchemeId': notification_scheme_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_notification_scheme(
        self,
        id: int,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> NotificationScheme:
        """GET /rest/api/3/notificationscheme/{id} — Get notification scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/notificationscheme/{id}',
            path_params={'id': id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, NotificationScheme)

    async def get_notification_scheme_to_project_mappings(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        notification_scheme_id: list[str] | None = None,
        project_id: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanNotificationSchemeAndProjectMappingJsonBean:
        """GET /rest/api/3/notificationscheme/project — Get projects using notification schemes paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/notificationscheme/project',
            query_params={'startAt': start_at, 'maxResults': max_results, 'notificationSchemeId': notification_scheme_id, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanNotificationSchemeAndProjectMappingJsonBean)

    async def get_notification_schemes(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id: list[str] | None = None,
        project_id: list[str] | None = None,
        only_default: bool | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanNotificationScheme:
        """GET /rest/api/3/notificationscheme — Get notification schemes paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/notificationscheme',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'projectId': project_id, 'onlyDefault': only_default, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanNotificationScheme)

    async def remove_notification_from_notification_scheme(
        self,
        notification_scheme_id: str,
        notification_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId} — Remove notification from notification scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId}',
            path_params={'notificationSchemeId': notification_scheme_id, 'notificationId': notification_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_notification_scheme(
        self,
        id: str,
        body: UpdateNotificationSchemeDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/notificationscheme/{id} — Update notification scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/notificationscheme/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
