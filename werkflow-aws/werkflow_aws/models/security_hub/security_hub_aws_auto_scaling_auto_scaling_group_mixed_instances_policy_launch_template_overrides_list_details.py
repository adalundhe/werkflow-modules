from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails(BaseModel):
    InstanceType: StrictStr | None = None
    WeightedCapacity: StrictStr | None = None
