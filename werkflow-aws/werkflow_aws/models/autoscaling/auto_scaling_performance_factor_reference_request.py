from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingPerformanceFactorReferenceRequest(BaseModel):
    InstanceFamily: StrictStr | None = None
