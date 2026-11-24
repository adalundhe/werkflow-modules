from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_anomaly_detector import CloudWatchLogsAnomalyDetector


class CloudWatchLogsListLogAnomalyDetectorsResponse(BaseModel):
    anomalyDetectors: list[CloudWatchLogsAnomalyDetector] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
