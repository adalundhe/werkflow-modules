from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_range import CloudWatchRange


class CloudWatchAnomalyDetectorConfiguration(BaseModel):
    ExcludedTimeRanges: list[CloudWatchRange] | None = None
    MetricTimezone: StrictStr | None = None
    AdaptationSpeed: StrictStr | None = None
    OutlierFilteringStrength: StrictStr | None = None
