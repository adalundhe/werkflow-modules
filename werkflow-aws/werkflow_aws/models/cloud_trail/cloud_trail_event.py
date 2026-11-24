from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_trail_resource import CloudTrailResource


class CloudTrailEvent(BaseModel):
    EventId: StrictStr | None = None
    EventName: StrictStr | None = None
    ReadOnly: StrictStr | None = None
    AccessKeyId: StrictStr | None = None
    EventTime: datetime.datetime | StrictStr | None = None
    EventSource: StrictStr | None = None
    Username: StrictStr | None = None
    Resources: list[CloudTrailResource] | None = None
    CloudTrailEvent: StrictStr | None = None
