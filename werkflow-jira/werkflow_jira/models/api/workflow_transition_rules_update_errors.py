from __future__ import annotations
from pydantic import BaseModel
from .workflow_transition_rules_update_error_details import WorkflowTransitionRulesUpdateErrorDetails


class WorkflowTransitionRulesUpdateErrors(BaseModel):
    updateResults: list[WorkflowTransitionRulesUpdateErrorDetails] | None = None
