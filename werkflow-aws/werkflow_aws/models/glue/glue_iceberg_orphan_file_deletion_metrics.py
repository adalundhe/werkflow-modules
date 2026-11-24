from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class GlueIcebergOrphanFileDeletionMetrics(BaseModel):
    NumberOfOrphanFilesDeleted: StrictInt | None = None
    DpuHours: StrictFloat | StrictInt | None = None
    NumberOfDpus: StrictInt | None = None
    JobDurationInHour: StrictFloat | StrictInt | None = None
