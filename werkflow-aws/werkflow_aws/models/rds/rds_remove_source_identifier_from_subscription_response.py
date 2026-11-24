from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_event_subscription import RDSEventSubscription


class RDSRemoveSourceIdentifierFromSubscriptionResponse(BaseModel):
    EventSubscription: RDSEventSubscription | None = None
    ResponseMetadata: dict[str, Any] | None = None
