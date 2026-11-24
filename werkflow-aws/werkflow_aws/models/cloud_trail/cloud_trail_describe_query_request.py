from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailDescribeQueryRequest(BaseModel):
    EventDataStore: StrictStr | None = None
    QueryId: StrictStr | None = None
    QueryAlias: StrictStr | None = None
    RefreshId: StrictStr | None = None
    EventDataStoreOwnerAccountId: StrictStr | None = None
