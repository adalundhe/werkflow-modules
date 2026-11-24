from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSCancelDBCapacityReservationRequest(BaseModel):
    DBCapacityReservationIdentifier: StrictStr
