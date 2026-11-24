from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowProjectIdScope(BaseModel):
    id: StrictStr | None = None
