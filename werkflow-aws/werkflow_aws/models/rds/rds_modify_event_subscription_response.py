from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_event_subscription import RDSEventSubscription


class RDSModifyEventSubscriptionResponse(BaseModel):
    EventSubscription: RDSEventSubscription | None = None
    ResponseMetadata: dict[str, Any] | None = None
