from __future__ import annotations
from pydantic import BaseModel
from .app_workflow_transition_rule import AppWorkflowTransitionRule
from .workflow_id import WorkflowId


class WorkflowTransitionRules(BaseModel):
    conditions: list[AppWorkflowTransitionRule] | None = None
    postFunctions: list[AppWorkflowTransitionRule] | None = None
    validators: list[AppWorkflowTransitionRule] | None = None
    workflowId: WorkflowId | None = None
