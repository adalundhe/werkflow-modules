from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_metric_stream_statistics_metric import CloudWatchMetricStreamStatisticsMetric


class CloudWatchMetricStreamStatisticsConfiguration(BaseModel):
    IncludeMetrics: list[CloudWatchMetricStreamStatisticsMetric] | None = None
    AdditionalStatistics: list[StrictStr] | None = None
