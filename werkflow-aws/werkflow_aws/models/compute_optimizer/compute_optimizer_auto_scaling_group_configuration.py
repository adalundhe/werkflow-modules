from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComputeOptimizerAutoScalingGroupConfiguration(BaseModel):
    desiredCapacity: StrictInt | None = None
    minSize: StrictInt | None = None
    maxSize: StrictInt | None = None
    instanceType: StrictStr | None = None
    allocationStrategy: StrictStr | None = None
    estimatedInstanceHourReductionPercentage: StrictFloat | StrictInt | None = None
    type: StrictStr | None = None
    mixedInstanceTypes: list[StrictStr] | None = None
