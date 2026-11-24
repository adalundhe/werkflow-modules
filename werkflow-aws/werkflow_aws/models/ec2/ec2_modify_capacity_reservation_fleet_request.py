from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ModifyCapacityReservationFleetRequest(BaseModel):
    CapacityReservationFleetId: StrictStr
    TotalTargetCapacity: StrictInt | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    DryRun: StrictBool | None = None
    RemoveEndDate: StrictBool | None = None
