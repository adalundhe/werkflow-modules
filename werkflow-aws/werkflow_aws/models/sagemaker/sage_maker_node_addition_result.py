from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerNodeAdditionResult(BaseModel):
    NodeLogicalId: StrictStr | None = None
    InstanceGroupName: StrictStr | None = None
    Status: StrictStr | None = None
    AvailabilityZones: list[StrictStr] | None = None
    InstanceTypes: list[StrictStr] | None = None
