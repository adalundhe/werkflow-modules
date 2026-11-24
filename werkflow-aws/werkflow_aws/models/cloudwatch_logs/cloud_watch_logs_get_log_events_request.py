from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudWatchLogsGetLogEventsRequest(BaseModel):
    logStreamName: StrictStr
    logGroupName: StrictStr | None = None
    logGroupIdentifier: StrictStr | None = None
    startTime: StrictInt | None = None
    endTime: StrictInt | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
    startFromHead: StrictBool | None = None
    unmask: StrictBool | None = None
