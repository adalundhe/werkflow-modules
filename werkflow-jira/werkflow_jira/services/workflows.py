from __future__ import annotations

from typing import Any
from ..models.api import (
    DefaultWorkflowEditorResponse,
    PageBeanWorkflow,
    WorkflowCapabilities,
    WorkflowCopyRequest,
    WorkflowCreateRequest,
    WorkflowCreateResponse,
    WorkflowCreateValidateRequest,
    WorkflowHistoryListRequest,
    WorkflowHistoryListResponseDTO,
    WorkflowHistoryReadRequest,
    WorkflowHistoryReadResponseDTO,
    WorkflowPreviewRequest,
    WorkflowPreviewResponse,
    WorkflowProjectIssueTypeUsageDTO,
    WorkflowProjectUsageDTO,
    WorkflowReadRequest,
    WorkflowReadResponse,
    WorkflowSchemeUsageDTO,
    WorkflowSearchResponse,
    WorkflowUpdateRequest,
    WorkflowUpdateResponse,
    WorkflowUpdateValidateRequestBean,
    WorkflowValidationErrorList,
)
from .base import JiraBaseService


class WorkflowsService(JiraBaseService):
    """Jira Cloud REST API v3 — Workflows (17 operations)."""

    async def copy_workflow(
        self,
        body: WorkflowCopyRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowCreateResponse:
        """POST /rest/api/3/workflows/copy — Copy workflow"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflows/copy',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowCreateResponse)

    async def create_workflows(
        self,
        body: WorkflowCreateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowCreateResponse:
        """POST /rest/api/3/workflows/create — Bulk create workflows"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflows/create',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowCreateResponse)

    async def delete_inactive_workflow(
        self,
        entity_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/workflow/{entityId} — Delete inactive workflow"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/workflow/{entityId}',
            path_params={'entityId': entity_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_default_editor(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> DefaultWorkflowEditorResponse:
        """GET /rest/api/3/workflows/defaultEditor — Get the user's default workflow editor"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflows/defaultEditor',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, DefaultWorkflowEditorResponse)

    async def get_project_usages_for_workflow(
        self,
        workflow_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowProjectUsageDTO:
        """GET /rest/api/3/workflow/{workflowId}/projectUsages — Get projects using a given workflow"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflow/{workflowId}/projectUsages',
            path_params={'workflowId': workflow_id},
            query_params={'nextPageToken': next_page_token, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowProjectUsageDTO)

    async def get_workflow_project_issue_type_usages(
        self,
        workflow_id: str,
        project_id: int,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowProjectIssueTypeUsageDTO:
        """GET /rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages — Get issue types in a project that are using a given workflow"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages',
            path_params={'workflowId': workflow_id, 'projectId': project_id},
            query_params={'nextPageToken': next_page_token, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowProjectIssueTypeUsageDTO)

    async def get_workflow_scheme_usages_for_workflow(
        self,
        workflow_id: str,
        *,
        next_page_token: str | None = None,
        max_results: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowSchemeUsageDTO:
        """GET /rest/api/3/workflow/{workflowId}/workflowSchemes — Get workflow schemes which are using a given workflow"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflow/{workflowId}/workflowSchemes',
            path_params={'workflowId': workflow_id},
            query_params={'nextPageToken': next_page_token, 'maxResults': max_results},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowSchemeUsageDTO)

    async def get_workflows_paginated(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        workflow_name: list[str] | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        is_active: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanWorkflow:
        """GET /rest/api/3/workflow/search — Get workflows paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflow/search',
            query_params={'startAt': start_at, 'maxResults': max_results, 'workflowName': workflow_name, 'expand': expand, 'queryString': query_string, 'orderBy': order_by, 'isActive': is_active},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanWorkflow)

    async def list_workflow_history(
        self,
        body: WorkflowHistoryListRequest | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowHistoryListResponseDTO:
        """POST /rest/api/3/workflow/history/list — List workflow history entries"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflow/history/list',
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowHistoryListResponseDTO)

    async def read_workflow_from_history(
        self,
        body: WorkflowHistoryReadRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowHistoryReadResponseDTO:
        """POST /rest/api/3/workflow/history — Read workflow version from history"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflow/history',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowHistoryReadResponseDTO)

    async def read_workflow_previews(
        self,
        body: WorkflowPreviewRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowPreviewResponse:
        """POST /rest/api/3/workflows/preview — Preview workflow"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflows/preview',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowPreviewResponse)

    async def read_workflows(
        self,
        body: WorkflowReadRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowReadResponse:
        """POST /rest/api/3/workflows — Bulk get workflows"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflows',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowReadResponse)

    async def search_workflows(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        expand: str | None = None,
        query_string: str | None = None,
        order_by: str | None = None,
        scope: str | None = None,
        is_active: bool | None = None,
        project_id: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowSearchResponse:
        """GET /rest/api/3/workflows/search — Search workflows"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflows/search',
            query_params={'startAt': start_at, 'maxResults': max_results, 'expand': expand, 'queryString': query_string, 'orderBy': order_by, 'scope': scope, 'isActive': is_active, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowSearchResponse)

    async def update_workflows(
        self,
        body: WorkflowUpdateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowUpdateResponse:
        """POST /rest/api/3/workflows/update — Bulk update workflows"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflows/update',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowUpdateResponse)

    async def validate_create_workflows(
        self,
        body: WorkflowCreateValidateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowValidationErrorList:
        """POST /rest/api/3/workflows/create/validation — Validate create workflows"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflows/create/validation',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowValidationErrorList)

    async def validate_update_workflows(
        self,
        body: WorkflowUpdateValidateRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowValidationErrorList:
        """POST /rest/api/3/workflows/update/validation — Validate update workflows"""
        response = await self._request(
            'POST',
            '/rest/api/3/workflows/update/validation',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowValidationErrorList)

    async def workflow_capabilities(
        self,
        *,
        workflow_id: str | None = None,
        project_id: str | None = None,
        issue_type_id: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowCapabilities:
        """GET /rest/api/3/workflows/capabilities — Get available workflow capabilities"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflows/capabilities',
            query_params={'workflowId': workflow_id, 'projectId': project_id, 'issueTypeId': issue_type_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowCapabilities)
