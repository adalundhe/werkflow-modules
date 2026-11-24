from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class GlueIcebergCompactionMetrics(BaseModel):
    NumberOfBytesCompacted: StrictInt | None = None
    NumberOfFilesCompacted: StrictInt | None = None
    DpuHours: StrictFloat | StrictInt | None = None
    NumberOfDpus: StrictInt | None = None
    JobDurationInHour: StrictFloat | StrictInt | None = None
