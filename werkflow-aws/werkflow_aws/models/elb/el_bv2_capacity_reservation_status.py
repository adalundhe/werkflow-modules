from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2CapacityReservationStatus(BaseModel):
    Code: StrictStr | None = None
    Reason: StrictStr | None = None
