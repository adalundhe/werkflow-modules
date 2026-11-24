from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel
from .workflow_transition_rule import WorkflowTransitionRule

if TYPE_CHECKING:
    from .workflow_condition import WorkflowCondition


class WorkflowRules(BaseModel):
    conditionsTree: WorkflowCondition | None = None
    postFunctions: list[WorkflowTransitionRule] | None = None
    validators: list[WorkflowTransitionRule] | None = None
