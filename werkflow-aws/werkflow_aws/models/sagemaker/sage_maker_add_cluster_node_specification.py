from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerAddClusterNodeSpecification(BaseModel):
    InstanceGroupName: StrictStr
    IncrementTargetCountBy: StrictInt
    AvailabilityZones: list[StrictStr] | None = None
    InstanceTypes: list[StrictStr] | None = None
