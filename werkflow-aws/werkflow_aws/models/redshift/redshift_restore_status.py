from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RedshiftRestoreStatus(BaseModel):
    Status: StrictStr | None = None
    CurrentRestoreRateInMegaBytesPerSecond: StrictFloat | StrictInt | None = None
    SnapshotSizeInMegaBytes: StrictInt | None = None
    ProgressInMegaBytes: StrictInt | None = None
    ElapsedTimeInSeconds: StrictInt | None = None
    EstimatedTimeToCompletionInSeconds: StrictInt | None = None
