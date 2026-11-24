from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingAvailabilityZoneDistribution(BaseModel):
    CapacityDistributionStrategy: StrictStr | None = None
