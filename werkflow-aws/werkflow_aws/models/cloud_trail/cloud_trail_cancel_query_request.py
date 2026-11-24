from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailCancelQueryRequest(BaseModel):
    QueryId: StrictStr
    EventDataStore: StrictStr | None = None
    EventDataStoreOwnerAccountId: StrictStr | None = None
