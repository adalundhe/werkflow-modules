from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationStackSetOperationPreferences(BaseModel):
    RegionConcurrencyType: StrictStr | None = None
    RegionOrder: list[StrictStr] | None = None
    FailureToleranceCount: StrictInt | None = None
    FailureTolerancePercentage: StrictInt | None = None
    MaxConcurrentCount: StrictInt | None = None
    MaxConcurrentPercentage: StrictInt | None = None
    ConcurrencyMode: StrictStr | None = None
