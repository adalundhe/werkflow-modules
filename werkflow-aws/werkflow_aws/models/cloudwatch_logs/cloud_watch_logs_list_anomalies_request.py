from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsListAnomaliesRequest(BaseModel):
    anomalyDetectorArn: StrictStr | None = None
    suppressionState: Literal['SUPPRESSED', 'UNSUPPRESSED'] | None = None
    limit: StrictInt | None = None
    nextToken: StrictStr | None = None
