from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class RDSDBCapacityReservationCommitmentInfo(BaseModel):
    CommittedCapacityPerAvailabilityZone: StrictInt | None = None
    CommitmentEndDate: datetime.datetime | StrictStr | None = None
