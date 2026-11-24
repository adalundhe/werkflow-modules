from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SecurityHubAwsRedshiftClusterRestoreStatus(BaseModel):
    CurrentRestoreRateInMegaBytesPerSecond: StrictFloat | StrictInt | None = None
    ElapsedTimeInSeconds: StrictInt | None = None
    EstimatedTimeToCompletionInSeconds: StrictInt | None = None
    ProgressInMegaBytes: StrictInt | None = None
    SnapshotSizeInMegaBytes: StrictInt | None = None
    Status: StrictStr | None = None
