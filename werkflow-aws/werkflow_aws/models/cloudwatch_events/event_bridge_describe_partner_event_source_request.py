from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDescribePartnerEventSourceRequest(BaseModel):
    Name: StrictStr
