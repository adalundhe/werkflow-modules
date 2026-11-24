from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamQueryDeleteScheduledQueryRequest(BaseModel):
    ScheduledQueryArn: StrictStr
