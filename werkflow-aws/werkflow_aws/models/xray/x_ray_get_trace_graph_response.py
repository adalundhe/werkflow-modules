from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_service import XRayService


class XRayGetTraceGraphResponse(BaseModel):
    Services: list[XRayService] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
