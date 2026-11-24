from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDeletePartnerEventSourceRequest(BaseModel):
    Name: StrictStr
    Account: StrictStr
