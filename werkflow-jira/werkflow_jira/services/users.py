from __future__ import annotations

from typing import Any
from ..models.api import (
    ColumnItem,
    GroupName,
    NewUserDetails,
    PageBeanUser,
    UnrestrictedUserEmail,
    User,
    UserColumnRequestBody,
    UserMigrationBean,
)
from .base import JiraBaseService


class UsersService(JiraBaseService):
    """Jira Cloud REST API v3 — Users (13 operations)."""

    async def bulk_get_users(
        self,
        account_id: list[str],
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        username: list[str] | None = None,
        key: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanUser:
        """GET /rest/api/3/user/bulk — Bulk get users"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/bulk',
            query_params={'startAt': start_at, 'maxResults': max_results, 'username': username, 'key': key, 'accountId': account_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanUser)

    async def bulk_get_users_migration(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        username: list[str] | None = None,
        key: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[UserMigrationBean]:
        """GET /rest/api/3/user/bulk/migration — Get account IDs for users"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/bulk/migration',
            query_params={'startAt': start_at, 'maxResults': max_results, 'username': username, 'key': key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, UserMigrationBean)

    async def create_user(
        self,
        body: NewUserDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> User:
        """POST /rest/api/3/user — Create user"""
        response = await self._request(
            'POST',
            '/rest/api/3/user',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, User)

    async def get_all_users(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[User]:
        """GET /rest/api/3/users/search — Get all users"""
        response = await self._request(
            'GET',
            '/rest/api/3/users/search',
            query_params={'startAt': start_at, 'maxResults': max_results, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, User)

    async def get_all_users_default(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[User]:
        """GET /rest/api/3/users — Get all users default"""
        response = await self._request(
            'GET',
            '/rest/api/3/users',
            query_params={'startAt': start_at, 'maxResults': max_results, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, User)

    async def get_user(
        self,
        *,
        account_id: str | None = None,
        username: str | None = None,
        key: str | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> User:
        """GET /rest/api/3/user — Get user"""
        response = await self._request(
            'GET',
            '/rest/api/3/user',
            query_params={'accountId': account_id, 'username': username, 'key': key, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, User)

    async def get_user_default_columns(
        self,
        *,
        account_id: str | None = None,
        username: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ColumnItem]:
        """GET /rest/api/3/user/columns — Get user default columns"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/columns',
            query_params={'accountId': account_id, 'username': username},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ColumnItem)

    async def get_user_email(
        self,
        account_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> UnrestrictedUserEmail:
        """GET /rest/api/3/user/email — Get user email"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/email',
            query_params={'accountId': account_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, UnrestrictedUserEmail)

    async def get_user_email_bulk(
        self,
        account_id: list[str],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> UnrestrictedUserEmail:
        """GET /rest/api/3/user/email/bulk — Get user email bulk"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/email/bulk',
            query_params={'accountId': account_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, UnrestrictedUserEmail)

    async def get_user_groups(
        self,
        account_id: str,
        *,
        username: str | None = None,
        key: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[GroupName]:
        """GET /rest/api/3/user/groups — Get user groups"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/groups',
            query_params={'accountId': account_id, 'username': username, 'key': key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, GroupName)

    async def remove_user(
        self,
        account_id: str,
        *,
        username: str | None = None,
        key: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/user — Delete user"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/user',
            query_params={'accountId': account_id, 'username': username, 'key': key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def reset_user_columns(
        self,
        *,
        account_id: str | None = None,
        username: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/user/columns — Reset user default columns"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/user/columns',
            query_params={'accountId': account_id, 'username': username},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def set_user_columns(
        self,
        body: UserColumnRequestBody | dict[str, Any],
        *,
        account_id: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/user/columns — Set user default columns"""
        response = await self._request(
            'PUT',
            '/rest/api/3/user/columns',
            query_params={'accountId': account_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
