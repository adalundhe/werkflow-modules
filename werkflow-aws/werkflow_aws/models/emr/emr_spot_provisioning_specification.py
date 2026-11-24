from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EMRSpotProvisioningSpecification(BaseModel):
    TimeoutDurationMinutes: StrictInt | None = None
    TimeoutAction: StrictStr | None = None
    BlockDurationMinutes: StrictInt | None = None
    AllocationStrategy: StrictStr | None = None
