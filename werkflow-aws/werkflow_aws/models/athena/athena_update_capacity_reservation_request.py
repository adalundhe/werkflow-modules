from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AthenaUpdateCapacityReservationRequest(BaseModel):
    TargetDpus: StrictInt
    Name: StrictStr
