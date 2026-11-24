from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSStartDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    DBCapacityReservationIdentifier: StrictStr | None = None
