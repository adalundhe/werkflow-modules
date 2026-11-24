from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowSchemeReadRequest(BaseModel):
    projectIds: list[StrictStr] | None = None
    workflowSchemeIds: list[StrictStr] | None = None
