from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .x_ray_root_cause_exception import XRayRootCauseException


class XRayFaultRootCauseEntity(BaseModel):
    Name: StrictStr | None = None
    Exceptions: list[XRayRootCauseException] | None = None
    Remote: StrictBool | None = None
