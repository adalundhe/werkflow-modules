from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeListReplaysRequest(BaseModel):
    NamePrefix: StrictStr | None = None
    State: Literal['STARTING', 'RUNNING', 'CANCELLING', 'COMPLETED', 'CANCELLED', 'FAILED'] | None = None
    EventSourceArn: StrictStr | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
