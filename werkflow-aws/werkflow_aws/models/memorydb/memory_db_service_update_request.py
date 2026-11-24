from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBServiceUpdateRequest(BaseModel):
    ServiceUpdateNameToApply: StrictStr | None = None
