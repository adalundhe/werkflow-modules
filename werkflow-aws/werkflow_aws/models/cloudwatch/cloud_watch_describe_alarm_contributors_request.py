from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchDescribeAlarmContributorsRequest(BaseModel):
    AlarmName: StrictStr
    NextToken: StrictStr | None = None
