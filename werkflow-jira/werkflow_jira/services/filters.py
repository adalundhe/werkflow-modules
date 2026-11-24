from __future__ import annotations

from typing import Any
from ..models.api import (
    ChangeFilterOwner,
    ColumnItem,
    ColumnRequestBody,
    Filter,
    PageBeanFilterDetails,
)
from .base import JiraBaseService


class FiltersService(JiraBaseService):
    """Jira Cloud REST API v3 — Filters (13 operations)."""

    async def change_filter_owner(
        self,
        id: int,
        body: ChangeFilterOwner | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/filter/{id}/owner — Change filter owner"""
        response = await self._request(
            'PUT',
            '/rest/api/3/filter/{id}/owner',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def create_filter(
        self,
        body: Filter | dict[str, Any],
        *,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Filter:
        """POST /rest/api/3/filter — Create filter"""
        response = await self._request(
            'POST',
            '/rest/api/3/filter',
            query_params={'expand': expand, 'overrideSharePermissions': override_share_permissions},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Filter)

    async def delete_favourite_for_filter(
        self,
        id: int,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Filter:
        """DELETE /rest/api/3/filter/{id}/favourite — Remove filter as favorite"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/filter/{id}/favourite',
            path_params={'id': id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Filter)

    async def delete_filter(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/filter/{id} — Delete filter"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/filter/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_columns(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[ColumnItem]:
        """GET /rest/api/3/filter/{id}/columns — Get columns"""
        response = await self._request(
            'GET',
            '/rest/api/3/filter/{id}/columns',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, ColumnItem)

    async def get_favourite_filters(
        self,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[Filter]:
        """GET /rest/api/3/filter/favourite — Get favorite filters"""
        response = await self._request(
            'GET',
            '/rest/api/3/filter/favourite',
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, Filter)

    async def get_filter(
        self,
        id: int,
        *,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Filter:
        """GET /rest/api/3/filter/{id} — Get filter"""
        response = await self._request(
            'GET',
            '/rest/api/3/filter/{id}',
            path_params={'id': id},
            query_params={'expand': expand, 'overrideSharePermissions': override_share_permissions},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Filter)

    async def get_filters_paginated(
        self,
        *,
        filter_name: str | None = None,
        account_id: str | None = None,
        owner: str | None = None,
        groupname: str | None = None,
        group_id: str | None = None,
        project_id: int | None = None,
        id: list[int] | None = None,
        order_by: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
        is_substring_match: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanFilterDetails:
        """GET /rest/api/3/filter/search — Search for filters"""
        response = await self._request(
            'GET',
            '/rest/api/3/filter/search',
            query_params={'filterName': filter_name, 'accountId': account_id, 'owner': owner, 'groupname': groupname, 'groupId': group_id, 'projectId': project_id, 'id': id, 'orderBy': order_by, 'startAt': start_at, 'maxResults': max_results, 'expand': expand, 'overrideSharePermissions': override_share_permissions, 'isSubstringMatch': is_substring_match},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanFilterDetails)

    async def get_my_filters(
        self,
        *,
        expand: str | None = None,
        include_favourites: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[Filter]:
        """GET /rest/api/3/filter/my — Get my filters"""
        response = await self._request(
            'GET',
            '/rest/api/3/filter/my',
            query_params={'expand': expand, 'includeFavourites': include_favourites},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, Filter)

    async def reset_columns(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/filter/{id}/columns — Reset columns"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/filter/{id}/columns',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def set_columns(
        self,
        id: int,
        body: ColumnRequestBody | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/filter/{id}/columns — Set columns"""
        response = await self._request(
            'PUT',
            '/rest/api/3/filter/{id}/columns',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def set_favourite_for_filter(
        self,
        id: int,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Filter:
        """PUT /rest/api/3/filter/{id}/favourite — Add filter as favorite"""
        response = await self._request(
            'PUT',
            '/rest/api/3/filter/{id}/favourite',
            path_params={'id': id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Filter)

    async def update_filter(
        self,
        id: int,
        body: Filter | dict[str, Any],
        *,
        expand: str | None = None,
        override_share_permissions: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Filter:
        """PUT /rest/api/3/filter/{id} — Update filter"""
        response = await self._request(
            'PUT',
            '/rest/api/3/filter/{id}',
            path_params={'id': id},
            query_params={'expand': expand, 'overrideSharePermissions': override_share_permissions},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Filter)
