from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InterruptionInfo(BaseModel):
    SourceCapacityReservationId: StrictStr | None = None
    InterruptionType: StrictStr | None = None
