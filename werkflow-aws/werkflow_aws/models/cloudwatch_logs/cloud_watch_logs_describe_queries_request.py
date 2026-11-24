from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeQueriesRequest(BaseModel):
    logGroupName: StrictStr | None = None
    status: Literal['Scheduled', 'Running', 'Complete', 'Failed', 'Cancelled', 'Timeout', 'Unknown'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    queryLanguage: Literal['CWLI', 'SQL', 'PPL'] | None = None
