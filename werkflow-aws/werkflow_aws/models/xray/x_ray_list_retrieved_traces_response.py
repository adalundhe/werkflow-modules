from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_retrieved_trace import XRayRetrievedTrace


class XRayListRetrievedTracesResponse(BaseModel):
    RetrievalStatus: StrictStr | None = None
    TraceFormat: StrictStr | None = None
    Traces: list[XRayRetrievedTrace] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
