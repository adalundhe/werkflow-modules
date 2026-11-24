from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_resource_metric_selection import CloudWatchResourceMetricSelection


class CloudWatchCreateResourceMetricsConfigurationRequest(BaseModel):
    ResourceArn: StrictStr
    MetricSelections: list[CloudWatchResourceMetricSelection] | None = None
