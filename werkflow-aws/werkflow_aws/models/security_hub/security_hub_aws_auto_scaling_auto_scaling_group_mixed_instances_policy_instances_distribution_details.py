from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails(BaseModel):
    OnDemandAllocationStrategy: StrictStr | None = None
    OnDemandBaseCapacity: StrictInt | None = None
    OnDemandPercentageAboveBaseCapacity: StrictInt | None = None
    SpotAllocationStrategy: StrictStr | None = None
    SpotInstancePools: StrictInt | None = None
    SpotMaxPrice: StrictStr | None = None
