from __future__ import annotations

from typing import Any
from ..models.api import (
    AvailableDashboardGadgetsResponse,
    BulkEditShareableEntityRequest,
    BulkEditShareableEntityResponse,
    Dashboard,
    DashboardDetails,
    DashboardGadget,
    DashboardGadgetResponse,
    DashboardGadgetSettings,
    DashboardGadgetUpdateRequest,
    EntityProperty,
    PageBeanDashboard,
    PageOfDashboards,
    PropertyKeys,
)
from .base import JiraBaseService


class DashboardsService(JiraBaseService):
    """Jira Cloud REST API v3 — Dashboards (17 operations)."""

    async def add_gadget(
        self,
        dashboard_id: int,
        body: DashboardGadgetSettings | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> DashboardGadget:
        """POST /rest/api/3/dashboard/{dashboardId}/gadget — Add gadget to dashboard"""
        response = await self._request(
            'POST',
            '/rest/api/3/dashboard/{dashboardId}/gadget',
            path_params={'dashboardId': dashboard_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, DashboardGadget)

    async def bulk_edit_dashboards(
        self,
        body: BulkEditShareableEntityRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkEditShareableEntityResponse:
        """PUT /rest/api/3/dashboard/bulk/edit — Bulk edit dashboards"""
        response = await self._request(
            'PUT',
            '/rest/api/3/dashboard/bulk/edit',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkEditShareableEntityResponse)

    async def copy_dashboard(
        self,
        id: str,
        body: DashboardDetails | dict[str, Any],
        *,
        extend_admin_permissions: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Dashboard:
        """POST /rest/api/3/dashboard/{id}/copy — Copy dashboard"""
        response = await self._request(
            'POST',
            '/rest/api/3/dashboard/{id}/copy',
            path_params={'id': id},
            query_params={'extendAdminPermissions': extend_admin_permissions},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Dashboard)

    async def create_dashboard(
        self,
        body: DashboardDetails | dict[str, Any],
        *,
        extend_admin_permissions: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Dashboard:
        """POST /rest/api/3/dashboard — Create dashboard"""
        response = await self._request(
            'POST',
            '/rest/api/3/dashboard',
            query_params={'extendAdminPermissions': extend_admin_permissions},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Dashboard)

    async def delete_dashboard(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/dashboard/{id} — Delete dashboard"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/dashboard/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_dashboard_item_property(
        self,
        dashboard_id: str,
        item_id: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} — Delete dashboard item property"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}',
            path_params={'dashboardId': dashboard_id, 'itemId': item_id, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_all_available_dashboard_gadgets(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> AvailableDashboardGadgetsResponse:
        """GET /rest/api/3/dashboard/gadgets — Get available gadgets"""
        response = await self._request(
            'GET',
            '/rest/api/3/dashboard/gadgets',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, AvailableDashboardGadgetsResponse)

    async def get_all_dashboards(
        self,
        *,
        filter: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageOfDashboards:
        """GET /rest/api/3/dashboard — Get all dashboards"""
        response = await self._request(
            'GET',
            '/rest/api/3/dashboard',
            query_params={'filter': filter, 'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageOfDashboards)

    async def get_all_gadgets(
        self,
        dashboard_id: int,
        *,
        module_key: list[str] | None = None,
        uri: list[str] | None = None,
        gadget_id: list[int] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> DashboardGadgetResponse:
        """GET /rest/api/3/dashboard/{dashboardId}/gadget — Get gadgets"""
        response = await self._request(
            'GET',
            '/rest/api/3/dashboard/{dashboardId}/gadget',
            path_params={'dashboardId': dashboard_id},
            query_params={'moduleKey': module_key, 'uri': uri, 'gadgetId': gadget_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, DashboardGadgetResponse)

    async def get_dashboard(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Dashboard:
        """GET /rest/api/3/dashboard/{id} — Get dashboard"""
        response = await self._request(
            'GET',
            '/rest/api/3/dashboard/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Dashboard)

    async def get_dashboard_item_property(
        self,
        dashboard_id: str,
        item_id: str,
        property_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> EntityProperty:
        """GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} — Get dashboard item property"""
        response = await self._request(
            'GET',
            '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}',
            path_params={'dashboardId': dashboard_id, 'itemId': item_id, 'propertyKey': property_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, EntityProperty)

    async def get_dashboard_item_property_keys(
        self,
        dashboard_id: str,
        item_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PropertyKeys:
        """GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties — Get dashboard item property keys"""
        response = await self._request(
            'GET',
            '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties',
            path_params={'dashboardId': dashboard_id, 'itemId': item_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PropertyKeys)

    async def get_dashboards_paginated(
        self,
        *,
        dashboard_name: str | None = None,
        account_id: str | None = None,
        owner: str | None = None,
        groupname: str | None = None,
        group_id: str | None = None,
        project_id: int | None = None,
        order_by: str | None = None,
        start_at: int | None = None,
        max_results: int | None = None,
        status: str | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanDashboard:
        """GET /rest/api/3/dashboard/search — Search for dashboards"""
        response = await self._request(
            'GET',
            '/rest/api/3/dashboard/search',
            query_params={'dashboardName': dashboard_name, 'accountId': account_id, 'owner': owner, 'groupname': groupname, 'groupId': group_id, 'projectId': project_id, 'orderBy': order_by, 'startAt': start_at, 'maxResults': max_results, 'status': status, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanDashboard)

    async def remove_gadget(
        self,
        dashboard_id: int,
        gadget_id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId} — Remove gadget from dashboard"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}',
            path_params={'dashboardId': dashboard_id, 'gadgetId': gadget_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def set_dashboard_item_property(
        self,
        dashboard_id: str,
        item_id: str,
        property_key: str,
        body: Any,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} — Set dashboard item property"""
        response = await self._request(
            'PUT',
            '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}',
            path_params={'dashboardId': dashboard_id, 'itemId': item_id, 'propertyKey': property_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_dashboard(
        self,
        id: str,
        body: DashboardDetails | dict[str, Any],
        *,
        extend_admin_permissions: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Dashboard:
        """PUT /rest/api/3/dashboard/{id} — Update dashboard"""
        response = await self._request(
            'PUT',
            '/rest/api/3/dashboard/{id}',
            path_params={'id': id},
            query_params={'extendAdminPermissions': extend_admin_permissions},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Dashboard)

    async def update_gadget(
        self,
        dashboard_id: int,
        gadget_id: int,
        body: DashboardGadgetUpdateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId} — Update gadget on dashboard"""
        response = await self._request(
            'PUT',
            '/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}',
            path_params={'dashboardId': dashboard_id, 'gadgetId': gadget_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
