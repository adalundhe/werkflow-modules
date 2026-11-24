from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AutoScalingSetInstanceHealthRequest(BaseModel):
    InstanceId: StrictStr
    HealthStatus: StrictStr
    ShouldRespectGracePeriod: StrictBool | None = None
