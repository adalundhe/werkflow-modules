from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaCancelCapacityReservationRequest(BaseModel):
    Name: StrictStr
