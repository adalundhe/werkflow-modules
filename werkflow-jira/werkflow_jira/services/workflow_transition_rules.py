from __future__ import annotations

from typing import Any
from ..models.api import (
    PageBeanWorkflowTransitionRules,
    WorkflowTransitionRulesUpdate,
    WorkflowTransitionRulesUpdateErrors,
    WorkflowsWithTransitionRulesDetails,
)
from .base import JiraBaseService


class WorkflowTransitionRulesService(JiraBaseService):
    """Jira Cloud REST API v3 — Workflow transition rules (3 operations)."""

    async def delete_workflow_transition_rule_configurations(
        self,
        body: WorkflowsWithTransitionRulesDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowTransitionRulesUpdateErrors:
        """PUT /rest/api/3/workflow/rule/config/delete — Delete workflow transition rule configurations"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflow/rule/config/delete',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowTransitionRulesUpdateErrors)

    async def get_workflow_transition_rule_configurations(
        self,
        types: list[str],
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        keys: list[str] | None = None,
        workflow_names: list[str] | None = None,
        with_tags: list[str] | None = None,
        draft: bool | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanWorkflowTransitionRules:
        """GET /rest/api/3/workflow/rule/config — Get workflow transition rule configurations"""
        response = await self._request(
            'GET',
            '/rest/api/3/workflow/rule/config',
            query_params={'startAt': start_at, 'maxResults': max_results, 'types': types, 'keys': keys, 'workflowNames': workflow_names, 'withTags': with_tags, 'draft': draft, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanWorkflowTransitionRules)

    async def update_workflow_transition_rule_configurations(
        self,
        body: WorkflowTransitionRulesUpdate | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> WorkflowTransitionRulesUpdateErrors:
        """PUT /rest/api/3/workflow/rule/config — Update workflow transition rule configurations"""
        response = await self._request(
            'PUT',
            '/rest/api/3/workflow/rule/config',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, WorkflowTransitionRulesUpdateErrors)
