from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2CapacityReservationCommitmentInfo(BaseModel):
    CommittedInstanceCount: StrictInt | None = None
    CommitmentEndDate: datetime.datetime | StrictStr | None = None
    CommitmentDuration: StrictInt | None = None
