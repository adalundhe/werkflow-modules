from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StatusWorkflowUsageWorkflow(BaseModel):
    id: StrictStr | None = None
