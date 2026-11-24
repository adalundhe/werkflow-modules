from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetLogAnomalyDetectorRequest(BaseModel):
    anomalyDetectorArn: StrictStr
