from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_event_subscription import DMSEventSubscription


class DMSDeleteEventSubscriptionResponse(BaseModel):
    EventSubscription: DMSEventSubscription | None = None
    ResponseMetadata: dict[str, Any] | None = None
