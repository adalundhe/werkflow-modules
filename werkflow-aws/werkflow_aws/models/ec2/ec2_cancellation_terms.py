from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2CancellationTerms(BaseModel):
    CancellationType: StrictStr | None = None
    ReservationState: StrictStr | None = None
    CommittedInstanceCount: StrictInt | None = None
    ChargeCommitmentDurationHours: StrictInt | None = None
    ChargeEndDate: datetime.datetime | StrictStr | None = None
