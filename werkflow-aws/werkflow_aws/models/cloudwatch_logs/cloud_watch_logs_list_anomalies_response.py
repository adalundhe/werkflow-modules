from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_anomaly import CloudWatchLogsAnomaly


class CloudWatchLogsListAnomaliesResponse(BaseModel):
    anomalies: list[CloudWatchLogsAnomaly] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
