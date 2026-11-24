from __future__ import annotations

from typing import Any
from ..models.api import (
    JExpEvaluateJiraExpressionResultBean,
    JiraExpressionEvalRequestBean,
    JiraExpressionEvaluateRequestBean,
    JiraExpressionForAnalysis,
    JiraExpressionResult,
    JiraExpressionsAnalysis,
)
from .base import JiraBaseService


class JiraExpressionsService(JiraBaseService):
    """Jira Cloud REST API v3 — Jira expressions (3 operations)."""

    async def analyse_expression(
        self,
        body: JiraExpressionForAnalysis | dict[str, Any],
        *,
        check: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> JiraExpressionsAnalysis:
        """POST /rest/api/3/expression/analyse — Analyse Jira expression"""
        response = await self._request(
            'POST',
            '/rest/api/3/expression/analyse',
            query_params={'check': check},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, JiraExpressionsAnalysis)

    async def evaluate_jsis_jira_expression(
        self,
        body: JiraExpressionEvaluateRequestBean | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> JExpEvaluateJiraExpressionResultBean:
        """POST /rest/api/3/expression/evaluate — Evaluate Jira expression using enhanced search API"""
        response = await self._request(
            'POST',
            '/rest/api/3/expression/evaluate',
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, JExpEvaluateJiraExpressionResultBean)

    async def evaluate_jira_expression(
        self,
        body: JiraExpressionEvalRequestBean | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> JiraExpressionResult:
        """POST /rest/api/3/expression/eval — Currently being removed. Evaluate Jira expression"""
        response = await self._request(
            'POST',
            '/rest/api/3/expression/eval',
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, JiraExpressionResult)
