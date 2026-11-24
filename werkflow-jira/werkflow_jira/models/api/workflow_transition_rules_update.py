from __future__ import annotations
from pydantic import BaseModel
from .workflow_transition_rules import WorkflowTransitionRules


class WorkflowTransitionRulesUpdate(BaseModel):
    workflows: list[WorkflowTransitionRules] | None = None
