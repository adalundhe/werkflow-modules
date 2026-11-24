from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class XRayStartTraceRetrievalRequest(BaseModel):
    TraceIds: list[StrictStr]
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
