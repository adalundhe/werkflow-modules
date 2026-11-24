from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeListPartnerEventSourceAccountsRequest(BaseModel):
    EventSourceName: StrictStr
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
