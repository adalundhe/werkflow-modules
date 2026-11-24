from __future__ import annotations

from typing import Any
from ..models.api import (
    ContainerOfWorkflowSchemeAssociations,
    WorkflowSchemeProjectAssociation,
)
from .base import JiraBaseService


class WorkflowSchemeProjectAssociationsService(JiraBaseService):
    """Jira Cloud REST API v3 — Workflow scheme project associations (2 operations)."""

    async def assign_scheme_to_project(
        self,
        body: WorkflowSchemeProjectAssociation | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/workflowscheme/project — Assign workflow scheme to project"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflowscheme/project',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_workflow_scheme_project_associations(
        self,
        project_id: list[int],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ContainerOfWorkflowSchemeAssociations:
        """GET /rest/api/3/workflowscheme/project — Get workflow scheme project associations"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme/project',
            query_params={'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ContainerOfWorkflowSchemeAssociations)
