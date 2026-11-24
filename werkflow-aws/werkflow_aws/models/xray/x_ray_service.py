from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .x_ray_edge import XRayEdge
from .x_ray_histogram_entry import XRayHistogramEntry
from .x_ray_service_statistics import XRayServiceStatistics


class XRayService(BaseModel):
    ReferenceId: StrictInt | None = None
    Name: StrictStr | None = None
    Names: list[StrictStr] | None = None
    Root: StrictBool | None = None
    AccountId: StrictStr | None = None
    Type: StrictStr | None = None
    State: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Edges: list[XRayEdge] | None = None
    SummaryStatistics: XRayServiceStatistics | None = None
    DurationHistogram: list[XRayHistogramEntry] | None = None
    ResponseTimeHistogram: list[XRayHistogramEntry] | None = None
