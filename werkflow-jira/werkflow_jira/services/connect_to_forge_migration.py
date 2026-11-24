from __future__ import annotations

from ..models.api import (
    TaskProgress,
)
from .base import JiraBaseService


class ConnectToForgeMigrationService(JiraBaseService):
    """Jira Cloud REST API v3 — Migration of Connect modules to Forge (2 operations)."""

    async def fetch_migration_task(
        self,
        connect_key: str,
        jira_issue_fields_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> TaskProgress:
        """GET /rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task — Get Connect issue field migration task"""
        response = await self._request(
            'GET',
            '/rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task',
            path_params={'connectKey': connect_key, 'jiraIssueFieldsKey': jira_issue_fields_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, TaskProgress)

    async def submit_task(
        self,
        connect_key: str,
        jira_issue_fields_key: str,
        *,
        retrigger_completed_migration: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """POST /rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task — Submit Connect issue field migration task"""
        response = await self._request(
            'POST',
            '/rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task',
            path_params={'connectKey': connect_key, 'jiraIssueFieldsKey': jira_issue_fields_key},
            query_params={'retriggerCompletedMigration': retrigger_completed_migration},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None
