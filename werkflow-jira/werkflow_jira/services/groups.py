from __future__ import annotations

from typing import Any
from ..models.api import (
    AddGroupBean,
    FoundGroups,
    Group,
    PageBeanGroupDetails,
    PageBeanUserDetails,
    UpdateUserToGroupBean,
)
from .base import JiraBaseService


class GroupsService(JiraBaseService):
    """Jira Cloud REST API v3 — Groups (8 operations)."""

    async def add_user_to_group(
        self,
        body: UpdateUserToGroupBean | dict[str, Any],
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Group:
        """POST /rest/api/3/group/user — Add user to group"""
        response = await self._request(
            'POST',
            '/rest/api/3/group/user',
            query_params={'groupname': groupname, 'groupId': group_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Group)

    async def bulk_get_groups(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        group_id: list[str] | None = None,
        group_name: list[str] | None = None,
        access_type: str | None = None,
        application_key: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanGroupDetails:
        """GET /rest/api/3/group/bulk — Bulk get groups"""
        response = await self._request(
            'GET',
            '/rest/api/3/group/bulk',
            query_params={'startAt': start_at, 'maxResults': max_results, 'groupId': group_id, 'groupName': group_name, 'accessType': access_type, 'applicationKey': application_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanGroupDetails)

    async def create_group(
        self,
        body: AddGroupBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Group:
        """POST /rest/api/3/group — Create group"""
        response = await self._request(
            'POST',
            '/rest/api/3/group',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Group)

    async def find_groups(
        self,
        *,
        account_id: str | None = None,
        query: str | None = None,
        exclude: list[str] | None = None,
        exclude_id: list[str] | None = None,
        max_results: int | None = None,
        case_insensitive: bool | None = None,
        user_name: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> FoundGroups:
        """GET /rest/api/3/groups/picker — Find groups"""
        response = await self._request(
            'GET',
            '/rest/api/3/groups/picker',
            query_params={'accountId': account_id, 'query': query, 'exclude': exclude, 'excludeId': exclude_id, 'maxResults': max_results, 'caseInsensitive': case_insensitive, 'userName': user_name},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, FoundGroups)

    async def get_group(
        self,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Group:
        """GET /rest/api/3/group — Get group"""
        response = await self._request(
            'GET',
            '/rest/api/3/group',
            query_params={'groupname': groupname, 'groupId': group_id, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Group)

    async def get_users_from_group(
        self,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        include_inactive_users: bool | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanUserDetails:
        """GET /rest/api/3/group/member — Get users from group"""
        response = await self._request(
            'GET',
            '/rest/api/3/group/member',
            query_params={'groupname': groupname, 'groupId': group_id, 'includeInactiveUsers': include_inactive_users, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanUserDetails)

    async def remove_group(
        self,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        swap_group: str | None = None,
        swap_group_id: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/group — Remove group"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/group',
            query_params={'groupname': groupname, 'groupId': group_id, 'swapGroup': swap_group, 'swapGroupId': swap_group_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def remove_user_from_group(
        self,
        account_id: str,
        *,
        groupname: str | None = None,
        group_id: str | None = None,
        username: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/group/user — Remove user from group"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/group/user',
            query_params={'groupname': groupname, 'groupId': group_id, 'username': username, 'accountId': account_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None
