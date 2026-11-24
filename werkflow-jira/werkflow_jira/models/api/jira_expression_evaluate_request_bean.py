from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_expression_evaluate_context_bean import JiraExpressionEvaluateContextBean


class JiraExpressionEvaluateRequestBean(BaseModel):
    context: JiraExpressionEvaluateContextBean | None = None
    expression: StrictStr | None = None
