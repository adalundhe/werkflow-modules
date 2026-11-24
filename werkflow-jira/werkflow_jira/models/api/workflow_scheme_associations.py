from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_scheme import WorkflowScheme


class WorkflowSchemeAssociations(BaseModel):
    projectIds: list[StrictStr] | None = None
    workflowScheme: WorkflowScheme | None = None
