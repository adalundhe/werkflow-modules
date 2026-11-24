from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_watch_metric_stream_filter import CloudWatchMetricStreamFilter
from .cloud_watch_metric_stream_statistics_configuration import CloudWatchMetricStreamStatisticsConfiguration
from .cloud_watch_tag_model import CloudWatchTagModel


class CloudWatchPutMetricStreamRequest(BaseModel):
    Name: StrictStr
    FirehoseArn: StrictStr
    RoleArn: StrictStr
    OutputFormat: Literal['json', 'opentelemetry0.7', 'opentelemetry1.0']
    IncludeFilters: list[CloudWatchMetricStreamFilter] | None = None
    ExcludeFilters: list[CloudWatchMetricStreamFilter] | None = None
    Tags: list[CloudWatchTagModel] | None = None
    StatisticsConfigurations: list[CloudWatchMetricStreamStatisticsConfiguration] | None = None
    IncludeLinkedAccountsMetrics: StrictBool | None = None
