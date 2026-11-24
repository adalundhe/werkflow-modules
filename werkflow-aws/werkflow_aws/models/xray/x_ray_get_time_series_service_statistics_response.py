from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .x_ray_time_series_service_statistics import XRayTimeSeriesServiceStatistics


class XRayGetTimeSeriesServiceStatisticsResponse(BaseModel):
    TimeSeriesServiceStatistics: list[XRayTimeSeriesServiceStatistics] | None = None
    ContainsOldGroupVersions: StrictBool | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
