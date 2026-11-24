from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class MemoryDBSlotMigration(BaseModel):
    ProgressPercentage: StrictFloat | StrictInt | None = None
