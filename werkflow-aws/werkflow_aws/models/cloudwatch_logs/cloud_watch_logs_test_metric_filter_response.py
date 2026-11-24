from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_metric_filter_match_record import CloudWatchLogsMetricFilterMatchRecord


class CloudWatchLogsTestMetricFilterResponse(BaseModel):
    matches: list[CloudWatchLogsMetricFilterMatchRecord] | None = None
    ResponseMetadata: dict[str, Any] | None = None
