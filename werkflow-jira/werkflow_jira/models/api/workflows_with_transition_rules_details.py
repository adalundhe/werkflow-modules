from __future__ import annotations
from pydantic import BaseModel
from .workflow_transition_rules_details import WorkflowTransitionRulesDetails


class WorkflowsWithTransitionRulesDetails(BaseModel):
    workflows: list[WorkflowTransitionRulesDetails] | None = None
