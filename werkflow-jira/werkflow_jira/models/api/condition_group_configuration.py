from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_rule_configuration import WorkflowRuleConfiguration


class ConditionGroupConfiguration(BaseModel):
    conditionGroups: list[ConditionGroupConfiguration] | None = None
    conditions: list[WorkflowRuleConfiguration] | None = None
    operation: StrictStr | None = None
