from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeSubscriptionFiltersRequest(BaseModel):
    logGroupName: StrictStr
    filterNamePrefix: StrictStr | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
