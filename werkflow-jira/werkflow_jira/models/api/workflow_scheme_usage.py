from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowSchemeUsage(BaseModel):
    id: StrictStr | None = None
