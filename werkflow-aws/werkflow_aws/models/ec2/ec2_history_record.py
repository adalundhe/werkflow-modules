from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_event_information import EC2EventInformation


class EC2HistoryRecord(BaseModel):
    EventInformation: EC2EventInformation | None = None
    EventType: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
