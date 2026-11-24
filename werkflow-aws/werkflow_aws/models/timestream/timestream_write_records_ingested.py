from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TimestreamWriteRecordsIngested(BaseModel):
    Total: StrictInt | None = None
    MemoryStore: StrictInt | None = None
    MagneticStore: StrictInt | None = None
