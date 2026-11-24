from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeReplayDestination(BaseModel):
    Arn: StrictStr | None = None
    FilterArns: list[StrictStr] | None = None
