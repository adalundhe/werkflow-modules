from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudWatchLogsDescribeLogStreamsRequest(BaseModel):
    logGroupName: StrictStr | None = None
    logGroupIdentifier: StrictStr | None = None
    logStreamNamePrefix: StrictStr | None = None
    orderBy: Literal['LogStreamName', 'LastEventTime'] | None = None
    descending: StrictBool | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
