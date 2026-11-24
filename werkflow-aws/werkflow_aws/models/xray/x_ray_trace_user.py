from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .x_ray_service_id import XRayServiceId


class XRayTraceUser(BaseModel):
    UserName: StrictStr | None = None
    ServiceIds: list[XRayServiceId] | None = None
