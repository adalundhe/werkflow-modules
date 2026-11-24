from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails(BaseModel):
    Value: StrictStr | None = None
