from __future__ import annotations

from typing import Any
from ..models.api import (
    BulkPolicyOperationResponse,
    BulkProjectPolicyRequest,
    PolicySummaryResponse,
    SetProjectPoliciesRequest,
    StatePolicyDocument,
    StatePolicyRule,
    ValidatePolicyRequest,
)
from .base import JiraBaseService


class PoliciesService(JiraBaseService):
    """Jira Cloud REST API v3 — Policies (7 operations)."""

    async def add_policy_to_projects(
        self,
        policy_id: str,
        body: BulkProjectPolicyRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkPolicyOperationResponse:
        """POST /rest/api/3/policies/{policyId}/apply — Apply a policy to projects"""
        response = await self._request(
            'POST',
            '/rest/api/3/policies/{policyId}/apply',
            path_params={'policyId': policy_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkPolicyOperationResponse)

    async def get_policy_state(
        self,
        project_id_or_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[StatePolicyDocument]:
        """GET /rest/api/3/policies/project/{projectIdOrKey} — Get project policy state"""
        response = await self._request(
            'GET',
            '/rest/api/3/policies/project/{projectIdOrKey}',
            path_params={'projectIdOrKey': project_id_or_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, StatePolicyDocument)

    async def get_project_rules(
        self,
        project_id_or_key: str,
        *,
        rule_type_ids: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[StatePolicyRule]:
        """GET /rest/api/3/policies/project/{projectIdOrKey}/rules — Get project policy rules"""
        response = await self._request(
            'GET',
            '/rest/api/3/policies/project/{projectIdOrKey}/rules',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'ruleTypeIds': rule_type_ids},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, StatePolicyRule)

    async def list_policies(
        self,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        cursor: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PolicySummaryResponse:
        """GET /rest/api/3/policies — Get all policies"""
        response = await self._request(
            'GET',
            '/rest/api/3/policies',
            query_params={'startAt': start_at, 'maxResults': max_results, 'cursor': cursor},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PolicySummaryResponse)

    async def remove_policy_from_projects(
        self,
        policy_id: str,
        body: BulkProjectPolicyRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> BulkPolicyOperationResponse:
        """POST /rest/api/3/policies/{policyId}/remove — Remove a policy from projects"""
        response = await self._request(
            'POST',
            '/rest/api/3/policies/{policyId}/remove',
            path_params={'policyId': policy_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, BulkPolicyOperationResponse)

    async def set_project_policies(
        self,
        project_id_or_key: str,
        body: SetProjectPoliciesRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/policies/project/{projectIdOrKey}/policies — Set the policies applied to a project"""
        response = await self._request(
            'PUT',
            '/rest/api/3/policies/project/{projectIdOrKey}/policies',
            path_params={'projectIdOrKey': project_id_or_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def validate_policy_application(
        self,
        project_id_or_key: str,
        body: ValidatePolicyRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/policies/project/{projectIdOrKey}/validate — Validate policy application to a project"""
        response = await self._request(
            'POST',
            '/rest/api/3/policies/project/{projectIdOrKey}/validate',
            path_params={'projectIdOrKey': project_id_or_key},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
