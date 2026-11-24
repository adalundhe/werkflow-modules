from __future__ import annotations
from pydantic import BaseModel
from .j_exp_evaluate_issues_meta_bean import JExpEvaluateIssuesMetaBean
from .jira_expressions_complexity_bean import JiraExpressionsComplexityBean


class JExpEvaluateMetaDataBean(BaseModel):
    complexity: JiraExpressionsComplexityBean | None = None
    issues: JExpEvaluateIssuesMetaBean | None = None
