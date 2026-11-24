from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_expression_eval_context_bean import JiraExpressionEvalContextBean


class JiraExpressionEvalRequestBean(BaseModel):
    context: JiraExpressionEvalContextBean | None = None
    expression: StrictStr | None = None
