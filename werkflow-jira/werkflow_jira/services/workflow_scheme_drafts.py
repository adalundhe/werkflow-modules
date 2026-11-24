from __future__ import annotations

from typing import Any
from ..models.api import (
    DefaultWorkflow,
    IssueTypeWorkflowMapping,
    IssueTypesWorkflowMapping,
    PublishDraftWorkflowScheme,
    WorkflowScheme,
)
from .base import JiraBaseService


class WorkflowSchemeDraftsService(JiraBaseService):
    """Jira Cloud REST API v3 — Workflow scheme drafts (14 operations)."""

    async def create_workflow_scheme_draft_from_parent(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """POST /rest/api/3/workflowscheme/{id}/createdraft — Create draft workflow scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflowscheme/{id}/createdraft',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def delete_draft_default_workflow(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """DELETE /rest/api/3/workflowscheme/{id}/draft/default — Delete draft default workflow"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/workflowscheme/{id}/draft/default',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def delete_draft_workflow_mapping(
        self,
        id: int,
        workflow_name: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/workflowscheme/{id}/draft/workflow — Delete issue types for workflow in draft workflow scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/workflowscheme/{id}/draft/workflow',
            path_params={'id': id},
            query_params={'workflowName': workflow_name},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_workflow_scheme_draft(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/workflowscheme/{id}/draft — Delete draft workflow scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/workflowscheme/{id}/draft',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_workflow_scheme_draft_issue_type(
        self,
        id: int,
        issue_type: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """DELETE /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType} — Delete workflow for issue type in draft workflow scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}',
            path_params={'id': id, 'issueType': issue_type},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def get_draft_default_workflow(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> DefaultWorkflow:
        """GET /rest/api/3/workflowscheme/{id}/draft/default — Get draft default workflow"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme/{id}/draft/default',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, DefaultWorkflow)

    async def get_draft_workflow(
        self,
        id: int,
        *,
        workflow_name: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueTypesWorkflowMapping:
        """GET /rest/api/3/workflowscheme/{id}/draft/workflow — Get issue types for workflows in draft workflow scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme/{id}/draft/workflow',
            path_params={'id': id},
            query_params={'workflowName': workflow_name},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueTypesWorkflowMapping)

    async def get_workflow_scheme_draft(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """GET /rest/api/3/workflowscheme/{id}/draft — Get draft workflow scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme/{id}/draft',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def get_workflow_scheme_draft_issue_type(
        self,
        id: int,
        issue_type: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueTypeWorkflowMapping:
        """GET /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType} — Get workflow for issue type in draft workflow scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}',
            path_params={'id': id, 'issueType': issue_type},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueTypeWorkflowMapping)

    async def publish_draft_workflow_scheme(
        self,
        id: int,
        body: PublishDraftWorkflowScheme | dict[str, Any],
        *,
        validate_only: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """POST /rest/api/3/workflowscheme/{id}/draft/publish — Publish draft workflow scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflowscheme/{id}/draft/publish',
            path_params={'id': id},
            query_params={'validateOnly': validate_only},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def set_workflow_scheme_draft_issue_type(
        self,
        id: int,
        issue_type: str,
        body: IssueTypeWorkflowMapping | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """PUT /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType} — Set workflow for issue type in draft workflow scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}',
            path_params={'id': id, 'issueType': issue_type},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def update_draft_default_workflow(
        self,
        id: int,
        body: DefaultWorkflow | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """PUT /rest/api/3/workflowscheme/{id}/draft/default — Update draft default workflow"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflowscheme/{id}/draft/default',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def update_draft_workflow_mapping(
        self,
        id: int,
        body: IssueTypesWorkflowMapping | dict[str, Any],
        workflow_name: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """PUT /rest/api/3/workflowscheme/{id}/draft/workflow — Set issue types for workflow in workflow scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflowscheme/{id}/draft/workflow',
            path_params={'id': id},
            query_params={'workflowName': workflow_name},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def update_workflow_scheme_draft(
        self,
        id: int,
        body: WorkflowScheme | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """PUT /rest/api/3/workflowscheme/{id}/draft — Update draft workflow scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflowscheme/{id}/draft',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)
