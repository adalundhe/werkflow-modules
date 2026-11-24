from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .jira_expression_complexity import JiraExpressionComplexity
from .jira_expression_validation_error import JiraExpressionValidationError


class JiraExpressionAnalysis(BaseModel):
    complexity: JiraExpressionComplexity | None = None
    errors: list[JiraExpressionValidationError] | None = None
    expression: StrictStr | None = None
    type: StrictStr | None = None
    valid: StrictBool | None = None
