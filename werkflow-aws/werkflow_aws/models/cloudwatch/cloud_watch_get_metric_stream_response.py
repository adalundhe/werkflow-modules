from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_watch_metric_stream_filter import CloudWatchMetricStreamFilter
from .cloud_watch_metric_stream_statistics_configuration import CloudWatchMetricStreamStatisticsConfiguration


class CloudWatchGetMetricStreamResponse(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    IncludeFilters: list[CloudWatchMetricStreamFilter] | None = None
    ExcludeFilters: list[CloudWatchMetricStreamFilter] | None = None
    FirehoseArn: StrictStr | None = None
    RoleArn: StrictStr | None = None
    State: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastUpdateDate: datetime.datetime | StrictStr | None = None
    OutputFormat: StrictStr | None = None
    StatisticsConfigurations: list[CloudWatchMetricStreamStatisticsConfiguration] | None = None
    IncludeLinkedAccountsMetrics: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
