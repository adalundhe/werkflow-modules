from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .x_ray_error_statistics import XRayErrorStatistics
from .x_ray_fault_statistics import XRayFaultStatistics


class XRayEdgeStatistics(BaseModel):
    OkCount: StrictInt | None = None
    ErrorStatistics: XRayErrorStatistics | None = None
    FaultStatistics: XRayFaultStatistics | None = None
    TotalCount: StrictInt | None = None
    TotalResponseTime: StrictFloat | StrictInt | None = None
