from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_metric_filter import CloudWatchLogsMetricFilter


class CloudWatchLogsDescribeMetricFiltersResponse(BaseModel):
    metricFilters: list[CloudWatchLogsMetricFilter] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
