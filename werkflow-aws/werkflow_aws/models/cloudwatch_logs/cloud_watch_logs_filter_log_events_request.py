from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudWatchLogsFilterLogEventsRequest(BaseModel):
    logGroupName: StrictStr | None = None
    logGroupIdentifier: StrictStr | None = None
    logStreamNames: list[StrictStr] | None = None
    logStreamNamePrefix: StrictStr | None = None
    startTime: StrictInt | None = None
    endTime: StrictInt | None = None
    filterPattern: StrictStr | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
    startFromHead: StrictBool | None = None
    interleaved: StrictBool | None = None
    unmask: StrictBool | None = None
