from __future__ import annotations

from typing import Any
from ..models.api import (
    BulkWorklogKeyRequestBean,
    BulkWorklogKeyResponseBean,
    ChangedWorklogs,
    PageOfWorklogs,
    Worklog,
    WorklogIdsRequestBean,
    WorklogsMoveRequestBean,
)
from .base import JiraBaseService


class IssueWorklogsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue worklogs (11 operations)."""

    async def add_worklog(
        self,
        issue_id_or_key: str,
        body: Worklog | dict[str, Any],
        *,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        reduce_by: str | None = None,
        expand: str | None = None,
        override_editable_flag: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Worklog:
        """POST /rest/api/3/issue/{issueIdOrKey}/worklog — Add worklog"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/{issueIdOrKey}/worklog',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'notifyUsers': notify_users, 'adjustEstimate': adjust_estimate, 'newEstimate': new_estimate, 'reduceBy': reduce_by, 'expand': expand, 'overrideEditableFlag': override_editable_flag},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Worklog)

    async def bulk_delete_worklogs(
        self,
        issue_id_or_key: str,
        body: WorklogIdsRequestBean | dict[str, Any],
        *,
        adjust_estimate: str | None = None,
        override_editable_flag: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/{issueIdOrKey}/worklog — Bulk delete worklogs"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/{issueIdOrKey}/worklog',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'adjustEstimate': adjust_estimate, 'overrideEditableFlag': override_editable_flag},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def bulk_move_worklogs(
        self,
        issue_id_or_key: str,
        body: WorklogsMoveRequestBean | dict[str, Any],
        *,
        adjust_estimate: str | None = None,
        override_editable_flag: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """POST /rest/api/3/issue/{issueIdOrKey}/worklog/move — Bulk move worklogs"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/{issueIdOrKey}/worklog/move',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'adjustEstimate': adjust_estimate, 'overrideEditableFlag': override_editable_flag},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_worklog(
        self,
        issue_id_or_key: str,
        id: str,
        *,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        increase_by: str | None = None,
        override_editable_flag: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{id} — Delete worklog"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/{issueIdOrKey}/worklog/{id}',
            path_params={'issueIdOrKey': issue_id_or_key, 'id': id},
            query_params={'notifyUsers': notify_users, 'adjustEstimate': adjust_estimate, 'newEstimate': new_estimate, 'increaseBy': increase_by, 'overrideEditableFlag': override_editable_flag},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_ids_of_worklogs_deleted_since(
        self,
        *,
        since: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ChangedWorklogs:
        """GET /rest/api/3/worklog/deleted — Get IDs of deleted worklogs"""
        response = await self._request(
            'GET',
            '/rest/api/3/worklog/deleted',
            query_params={'since': since},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ChangedWorklogs)

    async def get_ids_of_worklogs_modified_since(
        self,
        *,
        since: int | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ChangedWorklogs:
        """GET /rest/api/3/worklog/updated — Get IDs of updated worklogs"""
        response = await self._request(
            'GET',
            '/rest/api/3/worklog/updated',
            query_params={'since': since, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ChangedWorklogs)

    async def get_issue_worklog(
        self,
        issue_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        started_after: int | None = None,
        started_before: int | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageOfWorklogs:
        """GET /rest/api/3/issue/{issueIdOrKey}/worklog — Get issue worklogs"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/worklog',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'startAt': start_at, 'maxResults': max_results, 'startedAfter': started_after, 'startedBefore': started_before, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageOfWorklogs)

    async def get_worklog(
        self,
        issue_id_or_key: str,
        id: str,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Worklog:
        """GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id} — Get worklog"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/worklog/{id}',
            path_params={'issueIdOrKey': issue_id_or_key, 'id': id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Worklog)

    async def get_worklogs_by_issue_id_and_worklog_id(
        self,
        body: BulkWorklogKeyRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkWorklogKeyResponseBean:
        """POST /rest/internal/api/latest/worklog/bulk — Get worklogs by issue id and worklog id"""
        response = await self._request(
            'POST',
            '/rest/internal/api/latest/worklog/bulk',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkWorklogKeyResponseBean)

    async def get_worklogs_for_ids(
        self,
        body: WorklogIdsRequestBean | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[Worklog]:
        """POST /rest/api/3/worklog/list — Get worklogs"""
        response = await self._request(
            'POST',
            '/rest/api/3/worklog/list',
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, Worklog)

    async def update_worklog(
        self,
        issue_id_or_key: str,
        id: str,
        body: Worklog | dict[str, Any],
        *,
        notify_users: bool | None = None,
        adjust_estimate: str | None = None,
        new_estimate: str | None = None,
        expand: str | None = None,
        override_editable_flag: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Worklog:
        """PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{id} — Update worklog"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issue/{issueIdOrKey}/worklog/{id}',
            path_params={'issueIdOrKey': issue_id_or_key, 'id': id},
            query_params={'notifyUsers': notify_users, 'adjustEstimate': adjust_estimate, 'newEstimate': new_estimate, 'expand': expand, 'overrideEditableFlag': override_editable_flag},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Worklog)
