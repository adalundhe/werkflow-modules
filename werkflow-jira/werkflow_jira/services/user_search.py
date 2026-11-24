from __future__ import annotations

from ..models.api import (
    FoundUsers,
    PageBeanUser,
    PageBeanUserKey,
    User,
)
from .base import JiraBaseService


class UserSearchService(JiraBaseService):
    """Jira Cloud REST API v3 — User search (8 operations)."""

    async def find_assignable_users(
        self,
        *,
        query: str | None = None,
        session_id: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        project: str | None = None,
        issue_key: str | None = None,
        issue_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        action_descriptor_id: int | None = None,
        recommend: bool | None = None,
        account_type: list[str] | None = None,
        app_type: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[User]:
        """GET /rest/api/3/user/assignable/search — Find users assignable to issues"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/assignable/search',
            query_params={'query': query, 'sessionId': session_id, 'username': username, 'accountId': account_id, 'project': project, 'issueKey': issue_key, 'issueId': issue_id, 'startAt': start_at, 'maxResults': max_results, 'actionDescriptorId': action_descriptor_id, 'recommend': recommend, 'accountType': account_type, 'appType': app_type},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, User)

    async def find_bulk_assignable_users(
        self,
        project_keys: str,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[User]:
        """GET /rest/api/3/user/assignable/multiProjectSearch — Find users assignable to projects"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/assignable/multiProjectSearch',
            query_params={'query': query, 'username': username, 'accountId': account_id, 'projectKeys': project_keys, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, User)

    async def find_user_keys_by_query(
        self,
        query: str,
        *,
        start_at: int | None = None,
        max_result: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanUserKey:
        """GET /rest/api/3/user/search/query/key — Find user keys by query"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/search/query/key',
            query_params={'query': query, 'startAt': start_at, 'maxResult': max_result},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanUserKey)

    async def find_users(
        self,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        property: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[User]:
        """GET /rest/api/3/user/search — Find users"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/search',
            query_params={'query': query, 'username': username, 'accountId': account_id, 'startAt': start_at, 'maxResults': max_results, 'property': property},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, User)

    async def find_users_by_query(
        self,
        query: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanUser:
        """GET /rest/api/3/user/search/query — Find users by query"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/search/query',
            query_params={'query': query, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanUser)

    async def find_users_for_picker(
        self,
        query: str,
        *,
        max_results: int | None = None,
        show_avatar: bool | None = None,
        exclude: list[str] | None = None,
        exclude_account_ids: list[str] | None = None,
        avatar_size: str | None = None,
        exclude_connect_users: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> FoundUsers:
        """GET /rest/api/3/user/picker — Find users for picker"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/picker',
            query_params={'query': query, 'maxResults': max_results, 'showAvatar': show_avatar, 'exclude': exclude, 'excludeAccountIds': exclude_account_ids, 'avatarSize': avatar_size, 'excludeConnectUsers': exclude_connect_users},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, FoundUsers)

    async def find_users_with_all_permissions(
        self,
        permissions: str,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        issue_key: str | None = None,
        project_key: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[User]:
        """GET /rest/api/3/user/permission/search — Find users with permissions"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/permission/search',
            query_params={'query': query, 'username': username, 'accountId': account_id, 'permissions': permissions, 'issueKey': issue_key, 'projectKey': project_key, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, User)

    async def find_users_with_browse_permission(
        self,
        *,
        query: str | None = None,
        username: str | None = None,
        account_id: str | None = None,
        issue_key: str | None = None,
        project_key: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[User]:
        """GET /rest/api/3/user/viewissue/search — Find users with browse permission"""
        response = await self._request(
            'GET',
            '/rest/api/3/user/viewissue/search',
            query_params={'query': query, 'username': username, 'accountId': account_id, 'issueKey': issue_key, 'projectKey': project_key, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, User)
