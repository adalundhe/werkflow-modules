from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StatusesPerWorkflow(BaseModel):
    initialStatusId: StrictStr | None = None
    statuses: list[StrictStr] | None = None
    workflowId: StrictStr | None = None
