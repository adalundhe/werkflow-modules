from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeListEventBusesRequest(BaseModel):
    NamePrefix: StrictStr | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
