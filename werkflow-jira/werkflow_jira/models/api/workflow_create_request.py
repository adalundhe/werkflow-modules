from __future__ import annotations
from pydantic import BaseModel
from .workflow_create import WorkflowCreate
from .workflow_scope import WorkflowScope
from .workflow_status_update import WorkflowStatusUpdate


class WorkflowCreateRequest(BaseModel):
    scope: WorkflowScope | None = None
    statuses: list[WorkflowStatusUpdate] | None = None
    workflows: list[WorkflowCreate] | None = None
