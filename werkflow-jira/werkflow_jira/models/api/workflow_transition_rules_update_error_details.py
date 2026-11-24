from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_id import WorkflowId


class WorkflowTransitionRulesUpdateErrorDetails(BaseModel):
    ruleUpdateErrors: dict[StrictStr, list[StrictStr]] | None = None
    updateErrors: list[StrictStr] | None = None
    workflowId: WorkflowId | None = None
