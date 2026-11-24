from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsGetQueryResultsRequest(BaseModel):
    queryId: StrictStr
    nextToken: StrictStr | None = None
    maxItems: StrictInt | None = None
