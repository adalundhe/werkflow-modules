from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2InterruptibleCapacityAllocation(BaseModel):
    InstanceCount: StrictInt | None = None
    TargetInstanceCount: StrictInt | None = None
    Status: StrictStr | None = None
    InterruptibleCapacityReservationId: StrictStr | None = None
    InterruptionType: StrictStr | None = None
    ZeroSizePreference: StrictStr | None = None
