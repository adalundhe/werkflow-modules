from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyInstanceEventStartTimeRequest(BaseModel):
    InstanceId: StrictStr
    InstanceEventId: StrictStr
    NotBefore: datetime.datetime | StrictStr
    DryRun: StrictBool | None = None
