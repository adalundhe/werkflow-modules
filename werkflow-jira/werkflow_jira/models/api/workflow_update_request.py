from __future__ import annotations
from pydantic import BaseModel
from .workflow_status_update import WorkflowStatusUpdate
from .workflow_update import WorkflowUpdate


class WorkflowUpdateRequest(BaseModel):
    statuses: list[WorkflowStatusUpdate] | None = None
    workflows: list[WorkflowUpdate] | None = None
