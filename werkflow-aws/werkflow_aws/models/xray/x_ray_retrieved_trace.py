from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .x_ray_span import XRaySpan


class XRayRetrievedTrace(BaseModel):
    Id: StrictStr | None = None
    Duration: StrictFloat | StrictInt | None = None
    Spans: list[XRaySpan] | None = None
