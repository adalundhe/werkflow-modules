from __future__ import annotations

from typing import Any
from ..models.api import (
    TaskProgressBeanObject,
)
from .base import JiraBaseService


class TasksService(JiraBaseService):
    """Jira Cloud REST API v3 — Tasks (2 operations)."""

    async def cancel_task(
        self,
        task_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/task/{taskId}/cancel — Cancel task"""
        response = await self._request(
            'POST',
            '/rest/api/3/task/{taskId}/cancel',
            path_params={'taskId': task_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_task(
        self,
        task_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> TaskProgressBeanObject:
        """GET /rest/api/3/task/{taskId} — Get task"""
        response = await self._request(
            'GET',
            '/rest/api/3/task/{taskId}',
            path_params={'taskId': task_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, TaskProgressBeanObject)
