from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_event_subscription import NeptuneEventSubscription


class NeptuneModifyEventSubscriptionResponse(BaseModel):
    EventSubscription: NeptuneEventSubscription | None = None
    ResponseMetadata: dict[str, Any] | None = None
