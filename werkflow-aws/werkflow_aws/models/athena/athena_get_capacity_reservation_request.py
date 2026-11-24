from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaGetCapacityReservationRequest(BaseModel):
    Name: StrictStr
