from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DMSUpdateSubscriptionsToEventBridgeRequest(BaseModel):
    ForceMove: StrictBool | None = None
