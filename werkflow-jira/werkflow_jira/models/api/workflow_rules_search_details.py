from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_transition_rules import WorkflowTransitionRules


class WorkflowRulesSearchDetails(BaseModel):
    invalidRules: list[StrictStr] | None = None
    validRules: list[WorkflowTransitionRules] | None = None
    workflowEntityId: StrictStr | None = None
