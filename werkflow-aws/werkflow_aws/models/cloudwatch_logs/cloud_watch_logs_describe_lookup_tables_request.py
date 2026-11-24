from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeLookupTablesRequest(BaseModel):
    lookupTableNamePrefix: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
