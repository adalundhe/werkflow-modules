from __future__ import annotations
from pydantic import BaseModel
from .jira_expressions_complexity_value_bean import JiraExpressionsComplexityValueBean


class JiraExpressionsComplexityBean(BaseModel):
    beans: JiraExpressionsComplexityValueBean | None = None
    expensiveOperations: JiraExpressionsComplexityValueBean | None = None
    primitiveValues: JiraExpressionsComplexityValueBean | None = None
    steps: JiraExpressionsComplexityValueBean | None = None
