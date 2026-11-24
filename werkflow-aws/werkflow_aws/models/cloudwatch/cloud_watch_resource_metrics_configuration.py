from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_watch_resource_metric_selection import CloudWatchResourceMetricSelection


class CloudWatchResourceMetricsConfiguration(BaseModel):
    ResourceArn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    MetricSelections: list[CloudWatchResourceMetricSelection] | None = None
