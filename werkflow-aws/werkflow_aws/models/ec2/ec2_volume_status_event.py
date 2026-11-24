from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2VolumeStatusEvent(BaseModel):
    Description: StrictStr | None = None
    EventId: StrictStr | None = None
    EventType: StrictStr | None = None
    NotAfter: datetime.datetime | StrictStr | None = None
    NotBefore: datetime.datetime | StrictStr | None = None
    InstanceId: StrictStr | None = None
