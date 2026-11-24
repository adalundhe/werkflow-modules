from __future__ import annotations
from pydantic import BaseModel
from .x_ray_service_id import XRayServiceId


class XRayAnomalousService(BaseModel):
    ServiceId: XRayServiceId | None = None
