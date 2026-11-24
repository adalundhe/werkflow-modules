from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RDSModifyDBCapacityReservationRequest(BaseModel):
    DBCapacityReservationIdentifier: StrictStr
    CapacityPerAvailabilityZone: StrictInt | None = None
    EndDateType: Literal['unlimited', 'limited'] | None = None
    EndDate: datetime.datetime | StrictStr | None = None
