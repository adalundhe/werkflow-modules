from __future__ import annotations
from pydantic import BaseModel
from .jira_expression_analysis import JiraExpressionAnalysis


class JiraExpressionsAnalysis(BaseModel):
    results: list[JiraExpressionAnalysis] | None = None
