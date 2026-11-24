from __future__ import annotations
from pydantic import BaseModel, StrictBool


class WorkflowOperations(BaseModel):
    canDelete: StrictBool | None = None
    canEdit: StrictBool | None = None
