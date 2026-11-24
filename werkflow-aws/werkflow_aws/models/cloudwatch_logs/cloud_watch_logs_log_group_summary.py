from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsLogGroupSummary(BaseModel):
    logGroupName: StrictStr | None = None
    logGroupArn: StrictStr | None = None
    logGroupClass: StrictStr | None = None
