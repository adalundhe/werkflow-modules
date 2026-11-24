from __future__ import annotations
from pydantic import BaseModel
from .issues_meta_bean import IssuesMetaBean
from .jira_expressions_complexity_bean import JiraExpressionsComplexityBean


class JiraExpressionEvaluationMetaDataBean(BaseModel):
    complexity: JiraExpressionsComplexityBean | None = None
    issues: IssuesMetaBean | None = None
