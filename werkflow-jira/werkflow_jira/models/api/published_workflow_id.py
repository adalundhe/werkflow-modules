from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PublishedWorkflowId(BaseModel):
    entityId: StrictStr | None = None
    name: StrictStr | None = None
