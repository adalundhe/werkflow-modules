from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaDeleteCapacityReservationRequest(BaseModel):
    Name: StrictStr
