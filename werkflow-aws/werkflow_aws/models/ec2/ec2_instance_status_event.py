from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2InstanceStatusEvent(BaseModel):
    InstanceEventId: StrictStr | None = None
    Code: StrictStr | None = None
    Description: StrictStr | None = None
    NotAfter: datetime.datetime | StrictStr | None = None
    NotBefore: datetime.datetime | StrictStr | None = None
    NotBeforeDeadline: datetime.datetime | StrictStr | None = None
