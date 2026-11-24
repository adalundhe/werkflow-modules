from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .x_ray_error_root_cause_service import XRayErrorRootCauseService


class XRayErrorRootCause(BaseModel):
    Services: list[XRayErrorRootCauseService] | None = None
    ClientImpacting: StrictBool | None = None
