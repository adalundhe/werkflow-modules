from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_compute_limits import EMRComputeLimits


class EMRManagedScalingPolicy(BaseModel):
    ComputeLimits: EMRComputeLimits | None = None
    UtilizationPerformanceIndex: StrictInt | None = None
    ScalingStrategy: StrictStr | None = None
