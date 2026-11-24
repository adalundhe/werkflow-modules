from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2CapacityReservationAdjustmentDetails(BaseModel):
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    CommitmentEndDate: datetime.datetime | StrictStr | None = None
    EndDateType: StrictStr | None = None
    CommitmentDuration: StrictInt | None = None
