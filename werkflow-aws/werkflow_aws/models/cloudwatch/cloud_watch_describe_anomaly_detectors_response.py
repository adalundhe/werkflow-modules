from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_anomaly_detector import CloudWatchAnomalyDetector


class CloudWatchDescribeAnomalyDetectorsResponse(BaseModel):
    AnomalyDetectors: list[CloudWatchAnomalyDetector] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
