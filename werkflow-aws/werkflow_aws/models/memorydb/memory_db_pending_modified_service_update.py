from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBPendingModifiedServiceUpdate(BaseModel):
    ServiceUpdateName: StrictStr | None = None
    Status: StrictStr | None = None
