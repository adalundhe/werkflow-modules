from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerBatchAddClusterNodesError(BaseModel):
    InstanceGroupName: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    FailedCount: StrictInt | None = None
    AvailabilityZones: list[StrictStr] | None = None
    InstanceTypes: list[StrictStr] | None = None
    Message: StrictStr | None = None
