from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .x_ray_fault_root_cause_service import XRayFaultRootCauseService


class XRayFaultRootCause(BaseModel):
    Services: list[XRayFaultRootCauseService] | None = None
    ClientImpacting: StrictBool | None = None
