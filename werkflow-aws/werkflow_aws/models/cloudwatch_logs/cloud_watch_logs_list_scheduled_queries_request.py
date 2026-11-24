from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsListScheduledQueriesRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    state: Literal['ENABLED', 'DISABLED'] | None = None
    scheduleType: Literal['CUSTOMER_MANAGED', 'AWS_MANAGED'] | None = None
