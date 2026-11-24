from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .x_ray_response_time_root_cause_service import XRayResponseTimeRootCauseService


class XRayResponseTimeRootCause(BaseModel):
    Services: list[XRayResponseTimeRootCauseService] | None = None
    ClientImpacting: StrictBool | None = None
