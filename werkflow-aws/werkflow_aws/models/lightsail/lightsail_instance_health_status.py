from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_instance_health_status_detail import LightsailInstanceHealthStatusDetail


class LightsailInstanceHealthStatus(BaseModel):
    status: StrictStr | None = None
    details: list[LightsailInstanceHealthStatusDetail] | None = None
