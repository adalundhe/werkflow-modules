from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_id import WorkflowId


class WorkflowTransitionRulesDetails(BaseModel):
    workflowId: WorkflowId | None = None
    workflowRuleIds: list[StrictStr] | None = None
