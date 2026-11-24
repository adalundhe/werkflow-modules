from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_rule_configuration import WorkflowRuleConfiguration


class ConditionGroupUpdate(BaseModel):
    conditionGroups: list[ConditionGroupUpdate] | None = None
    conditions: list[WorkflowRuleConfiguration] | None = None
    operation: StrictStr | None = None
