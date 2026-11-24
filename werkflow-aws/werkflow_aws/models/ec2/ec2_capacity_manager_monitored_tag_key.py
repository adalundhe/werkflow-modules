from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CapacityManagerMonitoredTagKey(BaseModel):
    TagKey: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    CapacityManagerProvided: StrictBool | None = None
    EarliestDatapointTimestamp: datetime.datetime | StrictStr | None = None
