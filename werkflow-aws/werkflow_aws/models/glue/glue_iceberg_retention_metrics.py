from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class GlueIcebergRetentionMetrics(BaseModel):
    NumberOfDataFilesDeleted: StrictInt | None = None
    NumberOfManifestFilesDeleted: StrictInt | None = None
    NumberOfManifestListsDeleted: StrictInt | None = None
    DpuHours: StrictFloat | StrictInt | None = None
    NumberOfDpus: StrictInt | None = None
    JobDurationInHour: StrictFloat | StrictInt | None = None
