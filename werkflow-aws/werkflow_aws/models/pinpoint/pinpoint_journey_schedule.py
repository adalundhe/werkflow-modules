from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PinpointJourneySchedule(BaseModel):
    EndTime: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Timezone: StrictStr | None = None
