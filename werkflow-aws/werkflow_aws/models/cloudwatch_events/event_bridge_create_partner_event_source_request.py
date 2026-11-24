from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeCreatePartnerEventSourceRequest(BaseModel):
    Name: StrictStr
    Account: StrictStr
