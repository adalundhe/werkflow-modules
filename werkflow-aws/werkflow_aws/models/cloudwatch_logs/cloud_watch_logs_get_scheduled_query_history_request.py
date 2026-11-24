from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsGetScheduledQueryHistoryRequest(BaseModel):
    identifier: StrictStr
    startTime: StrictInt
    endTime: StrictInt
    executionStatuses: list[Literal['Running', 'InvalidQuery', 'Complete', 'Failed', 'Timeout']] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
