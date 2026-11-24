from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .x_ray_segment import XRaySegment


class XRayTrace(BaseModel):
    Id: StrictStr | None = None
    Duration: StrictFloat | StrictInt | None = None
    LimitExceeded: StrictBool | None = None
    Segments: list[XRaySegment] | None = None
