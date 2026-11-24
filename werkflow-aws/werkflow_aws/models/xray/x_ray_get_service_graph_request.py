from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class XRayGetServiceGraphRequest(BaseModel):
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    GroupName: StrictStr | None = None
    GroupARN: StrictStr | None = None
    NextToken: StrictStr | None = None
