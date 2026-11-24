from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ModificationQuoteCurrentConfiguration(BaseModel):
    InstanceCount: StrictInt | None = None
    ReservationState: StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    OriginalStartDate: datetime.datetime | StrictStr | None = None
