from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .x_ray_edge_statistics import XRayEdgeStatistics
from .x_ray_forecast_statistics import XRayForecastStatistics
from .x_ray_histogram_entry import XRayHistogramEntry
from .x_ray_service_statistics import XRayServiceStatistics


class XRayTimeSeriesServiceStatistics(BaseModel):
    Timestamp: datetime.datetime | StrictStr | None = None
    EdgeSummaryStatistics: XRayEdgeStatistics | None = None
    ServiceSummaryStatistics: XRayServiceStatistics | None = None
    ServiceForecastStatistics: XRayForecastStatistics | None = None
    ResponseTimeHistogram: list[XRayHistogramEntry] | None = None
