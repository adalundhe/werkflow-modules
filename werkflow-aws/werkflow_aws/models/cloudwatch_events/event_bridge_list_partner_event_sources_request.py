from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeListPartnerEventSourcesRequest(BaseModel):
    NamePrefix: StrictStr
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
