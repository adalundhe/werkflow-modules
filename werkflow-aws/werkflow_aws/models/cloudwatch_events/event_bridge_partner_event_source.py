from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgePartnerEventSource(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
