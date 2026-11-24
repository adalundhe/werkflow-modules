from __future__ import annotations

from typing import Any
from ..models.api import (
    DefaultWorkflow,
    IssueTypeWorkflowMapping,
    IssueTypesWorkflowMapping,
    PageBeanWorkflowScheme,
    WorkflowScheme,
    WorkflowSchemeProjectSwitchBean,
    WorkflowSchemeProjectUsageDTO,
    WorkflowSchemeReadRequest,
    WorkflowSchemeReadResponse,
    WorkflowSchemeUpdateRequest,
    WorkflowSchemeUpdateRequiredMappingsRequest,
    WorkflowSchemeUpdateRequiredMappingsResponse,
)
from .base import JiraBaseService


class WorkflowSchemesService(JiraBaseService):
    """Jira Cloud REST API v3 — Workflow schemes (19 operations)."""

    async def create_workflow_scheme(
        self,
        body: WorkflowScheme | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """POST /rest/api/3/workflowscheme — Create workflow scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflowscheme',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def delete_default_workflow(
        self,
        id: int,
        *,
        update_draft_if_needed: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """DELETE /rest/api/3/workflowscheme/{id}/default — Delete default workflow"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/workflowscheme/{id}/default',
            path_params={'id': id},
            query_params={'updateDraftIfNeeded': update_draft_if_needed},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def delete_workflow_mapping(
        self,
        id: int,
        workflow_name: str,
        *,
        update_draft_if_needed: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/workflowscheme/{id}/workflow — Delete issue types for workflow in workflow scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/workflowscheme/{id}/workflow',
            path_params={'id': id},
            query_params={'workflowName': workflow_name, 'updateDraftIfNeeded': update_draft_if_needed},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_workflow_scheme(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/workflowscheme/{id} — Delete workflow scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/workflowscheme/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def delete_workflow_scheme_issue_type(
        self,
        id: int,
        issue_type: str,
        *,
        update_draft_if_needed: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """DELETE /rest/api/3/workflowscheme/{id}/issuetype/{issueType} — Delete workflow for issue type in workflow scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/workflowscheme/{id}/issuetype/{issueType}',
            path_params={'id': id, 'issueType': issue_type},
            query_params={'updateDraftIfNeeded': update_draft_if_needed},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def get_all_workflow_schemes(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanWorkflowScheme:
        """GET /rest/api/3/workflowscheme — Get all workflow schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme',
            query_params={'startAt': start_at, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanWorkflowScheme)

    async def get_default_workflow(
        self,
        id: int,
        *,
        return_draft_if_exists: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> DefaultWorkflow:
        """GET /rest/api/3/workflowscheme/{id}/default — Get default workflow"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme/{id}/default',
            path_params={'id': id},
            query_params={'returnDraftIfExists': return_draft_if_exists},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, DefaultWorkflow)

    async def get_project_usages_for_workflow_scheme(
        self,
        workflow_scheme_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowSchemeProjectUsageDTO:
        """GET /rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages — Get projects which are using a given workflow scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages',
            path_params={'workflowSchemeId': workflow_scheme_id},
            query_params={'nextPageToken': next_page_token, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowSchemeProjectUsageDTO)

    async def get_required_workflow_scheme_mappings(
        self,
        body: WorkflowSchemeUpdateRequiredMappingsRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowSchemeUpdateRequiredMappingsResponse:
        """POST /rest/api/3/workflowscheme/update/mappings — Get required status mappings for workflow scheme update"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflowscheme/update/mappings',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowSchemeUpdateRequiredMappingsResponse)

    async def get_workflow(
        self,
        id: int,
        *,
        workflow_name: str | None = None,
        return_draft_if_exists: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueTypesWorkflowMapping:
        """GET /rest/api/3/workflowscheme/{id}/workflow — Get issue types for workflows in workflow scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme/{id}/workflow',
            path_params={'id': id},
            query_params={'workflowName': workflow_name, 'returnDraftIfExists': return_draft_if_exists},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueTypesWorkflowMapping)

    async def get_workflow_scheme(
        self,
        id: int,
        *,
        return_draft_if_exists: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """GET /rest/api/3/workflowscheme/{id} — Get workflow scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme/{id}',
            path_params={'id': id},
            query_params={'returnDraftIfExists': return_draft_if_exists},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def get_workflow_scheme_issue_type(
        self,
        id: int,
        issue_type: str,
        *,
        return_draft_if_exists: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> IssueTypeWorkflowMapping:
        """GET /rest/api/3/workflowscheme/{id}/issuetype/{issueType} — Get workflow for issue type in workflow scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflowscheme/{id}/issuetype/{issueType}',
            path_params={'id': id, 'issueType': issue_type},
            query_params={'returnDraftIfExists': return_draft_if_exists},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, IssueTypeWorkflowMapping)

    async def read_workflow_schemes(
        self,
        body: WorkflowSchemeReadRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[WorkflowSchemeReadResponse]:
        """POST /rest/api/3/workflowscheme/read — Bulk get workflow schemes"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflowscheme/read',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, WorkflowSchemeReadResponse)

    async def set_workflow_scheme_issue_type(
        self,
        id: int,
        issue_type: str,
        body: IssueTypeWorkflowMapping | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """PUT /rest/api/3/workflowscheme/{id}/issuetype/{issueType} — Set workflow for issue type in workflow scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflowscheme/{id}/issuetype/{issueType}',
            path_params={'id': id, 'issueType': issue_type},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def switch_workflow_scheme_for_project(
        self,
        body: WorkflowSchemeProjectSwitchBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """POST /rest/api/3/workflowscheme/project/switch — Switch workflow scheme for project"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflowscheme/project/switch',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def update_default_workflow(
        self,
        id: int,
        body: DefaultWorkflow | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """PUT /rest/api/3/workflowscheme/{id}/default — Update default workflow"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflowscheme/{id}/default',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def update_schemes(
        self,
        body: WorkflowSchemeUpdateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/workflowscheme/update — Update workflow scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflowscheme/update',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_workflow_mapping(
        self,
        id: int,
        body: IssueTypesWorkflowMapping | dict[str, Any],
        workflow_name: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """PUT /rest/api/3/workflowscheme/{id}/workflow — Set issue types for workflow in workflow scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflowscheme/{id}/workflow',
            path_params={'id': id},
            query_params={'workflowName': workflow_name},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)

    async def update_workflow_scheme(
        self,
        id: int,
        body: WorkflowScheme | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowScheme:
        """PUT /rest/api/3/workflowscheme/{id} — Classic update workflow scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflowscheme/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowScheme)
