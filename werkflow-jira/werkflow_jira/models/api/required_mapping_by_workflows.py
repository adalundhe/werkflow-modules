from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RequiredMappingByWorkflows(BaseModel):
    sourceWorkflowId: StrictStr | None = None
    statusIds: list[StrictStr] | None = None
    targetWorkflowId: StrictStr | None = None
