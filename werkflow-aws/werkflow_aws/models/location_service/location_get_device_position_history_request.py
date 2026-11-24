from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class LocationGetDevicePositionHistoryRequest(BaseModel):
    TrackerName: StrictStr
    DeviceId: StrictStr
    NextToken: StrictStr | None = None
    StartTimeInclusive: datetime.datetime | StrictStr | None = None
    EndTimeExclusive: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
