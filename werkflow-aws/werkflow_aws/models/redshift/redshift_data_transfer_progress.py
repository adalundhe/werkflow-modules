from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RedshiftDataTransferProgress(BaseModel):
    Status: StrictStr | None = None
    CurrentRateInMegaBytesPerSecond: StrictFloat | StrictInt | None = None
    TotalDataInMegaBytes: StrictInt | None = None
    DataTransferredInMegaBytes: StrictInt | None = None
    EstimatedTimeToCompletionInSeconds: StrictInt | None = None
    ElapsedTimeInSeconds: StrictInt | None = None
