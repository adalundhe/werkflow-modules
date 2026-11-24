from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ModificationReservationUpdate(BaseModel):
    NewCommitmentEndDate: datetime.datetime | StrictStr | None = None
    NewStartDate: datetime.datetime | StrictStr | None = None
    NewCommitmentDuration: StrictInt | None = None
