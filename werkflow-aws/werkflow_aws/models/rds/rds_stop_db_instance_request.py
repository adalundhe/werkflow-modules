from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSStopDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    DBSnapshotIdentifier: StrictStr | None = None
    DetachFromDBCapacityReservation: StrictBool | None = None
