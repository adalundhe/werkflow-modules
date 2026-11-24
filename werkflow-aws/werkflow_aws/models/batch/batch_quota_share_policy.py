from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchQuotaSharePolicy(BaseModel):
    idleResourceAssignmentStrategy: StrictStr | None = None
