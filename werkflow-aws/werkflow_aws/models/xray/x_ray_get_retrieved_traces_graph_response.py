from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_retrieved_service import XRayRetrievedService


class XRayGetRetrievedTracesGraphResponse(BaseModel):
    RetrievalStatus: StrictStr | None = None
    Services: list[XRayRetrievedService] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
