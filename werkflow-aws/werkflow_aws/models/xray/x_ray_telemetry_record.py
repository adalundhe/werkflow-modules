from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .x_ray_backend_connection_errors import XRayBackendConnectionErrors


class XRayTelemetryRecord(BaseModel):
    Timestamp: datetime.datetime | StrictStr
    SegmentsReceivedCount: StrictInt | None = None
    SegmentsSentCount: StrictInt | None = None
    SegmentsSpilloverCount: StrictInt | None = None
    SegmentsRejectedCount: StrictInt | None = None
    BackendConnectionErrors: XRayBackendConnectionErrors | None = None
