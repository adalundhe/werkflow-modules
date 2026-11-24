from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudTrailGetQueryResultsRequest(BaseModel):
    QueryId: StrictStr
    EventDataStore: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxQueryResults: StrictInt | None = None
    EventDataStoreOwnerAccountId: StrictStr | None = None
