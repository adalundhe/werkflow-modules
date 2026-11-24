from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamQueryDescribeScheduledQueryRequest(BaseModel):
    ScheduledQueryArn: StrictStr
