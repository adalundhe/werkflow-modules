from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeCondition(BaseModel):
    Type: StrictStr
    Key: StrictStr
    Value: StrictStr
