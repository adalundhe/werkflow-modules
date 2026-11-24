from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingLaunchInstancesError(BaseModel):
    InstanceType: StrictStr | None = None
    MarketType: StrictStr | None = None
    SubnetId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
