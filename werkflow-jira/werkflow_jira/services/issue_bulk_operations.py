from __future__ import annotations

from typing import Any
from ..models.api import (
    BulkEditGetFields,
    BulkOperationProgress,
    BulkTransitionGetAvailableTransitions,
    IssueBulkDeletePayload,
    IssueBulkEditPayload,
    IssueBulkMovePayload,
    IssueBulkTransitionPayload,
    IssueBulkWatchOrUnwatchPayload,
    SubmittedBulkOperation,
)
from .base import JiraBaseService


class IssueBulkOperationsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue bulk operations (9 operations)."""

    async def get_available_transitions(
        self,
        issue_ids_or_keys: str,
        *,
        ending_before: str | None = None,
        starting_after: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkTransitionGetAvailableTransitions:
        """GET /rest/api/3/bulk/issues/transition — Get available transitions"""
        response = await self._request(
            'GET',
            '/rest/api/3/bulk/issues/transition',
            query_params={'issueIdsOrKeys': issue_ids_or_keys, 'endingBefore': ending_before, 'startingAfter': starting_after},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkTransitionGetAvailableTransitions)

    async def get_bulk_editable_fields(
        self,
        issue_ids_or_keys: str,
        *,
        search_text: str | None = None,
        ending_before: str | None = None,
        starting_after: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkEditGetFields:
        """GET /rest/api/3/bulk/issues/fields — Get bulk editable fields"""
        response = await self._request(
            'GET',
            '/rest/api/3/bulk/issues/fields',
            query_params={'issueIdsOrKeys': issue_ids_or_keys, 'searchText': search_text, 'endingBefore': ending_before, 'startingAfter': starting_after},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkEditGetFields)

    async def get_bulk_operation_progress(
        self,
        task_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkOperationProgress:
        """GET /rest/api/3/bulk/queue/{taskId} — Get bulk issue operation progress"""
        response = await self._request(
            'GET',
            '/rest/api/3/bulk/queue/{taskId}',
            path_params={'taskId': task_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkOperationProgress)

    async def submit_bulk_delete(
        self,
        body: IssueBulkDeletePayload | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SubmittedBulkOperation:
        """POST /rest/api/3/bulk/issues/delete — Bulk delete issues"""
        response = await self._request(
            'POST',
            '/rest/api/3/bulk/issues/delete',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SubmittedBulkOperation)

    async def submit_bulk_edit(
        self,
        body: IssueBulkEditPayload | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SubmittedBulkOperation:
        """POST /rest/api/3/bulk/issues/fields — Bulk edit issues"""
        response = await self._request(
            'POST',
            '/rest/api/3/bulk/issues/fields',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SubmittedBulkOperation)

    async def submit_bulk_move(
        self,
        body: IssueBulkMovePayload | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SubmittedBulkOperation:
        """POST /rest/api/3/bulk/issues/move — Bulk move issues"""
        response = await self._request(
            'POST',
            '/rest/api/3/bulk/issues/move',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SubmittedBulkOperation)

    async def submit_bulk_transition(
        self,
        body: IssueBulkTransitionPayload | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SubmittedBulkOperation:
        """POST /rest/api/3/bulk/issues/transition — Bulk transition issue statuses"""
        response = await self._request(
            'POST',
            '/rest/api/3/bulk/issues/transition',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SubmittedBulkOperation)

    async def submit_bulk_unwatch(
        self,
        body: IssueBulkWatchOrUnwatchPayload | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SubmittedBulkOperation:
        """POST /rest/api/3/bulk/issues/unwatch — Bulk unwatch issues"""
        response = await self._request(
            'POST',
            '/rest/api/3/bulk/issues/unwatch',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SubmittedBulkOperation)

    async def submit_bulk_watch(
        self,
        body: IssueBulkWatchOrUnwatchPayload | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SubmittedBulkOperation:
        """POST /rest/api/3/bulk/issues/watch — Bulk watch issues"""
        response = await self._request(
            'POST',
            '/rest/api/3/bulk/issues/watch',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SubmittedBulkOperation)
