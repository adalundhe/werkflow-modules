from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .x_ray_alias import XRayAlias
from .x_ray_edge_statistics import XRayEdgeStatistics
from .x_ray_histogram_entry import XRayHistogramEntry


class XRayEdge(BaseModel):
    ReferenceId: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    SummaryStatistics: XRayEdgeStatistics | None = None
    ResponseTimeHistogram: list[XRayHistogramEntry] | None = None
    Aliases: list[XRayAlias] | None = None
    EdgeType: StrictStr | None = None
    ReceivedEventAgeHistogram: list[XRayHistogramEntry] | None = None
