from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class EC2CreateInterruptibleCapacityReservationAllocationResponse(BaseModel):
    SourceCapacityReservationId: StrictStr | None = None
    TargetInstanceCount: StrictInt | None = None
    Status: StrictStr | None = None
    InterruptionType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
