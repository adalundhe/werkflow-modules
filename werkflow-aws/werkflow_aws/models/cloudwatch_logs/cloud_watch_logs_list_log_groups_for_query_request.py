from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsListLogGroupsForQueryRequest(BaseModel):
    queryId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
