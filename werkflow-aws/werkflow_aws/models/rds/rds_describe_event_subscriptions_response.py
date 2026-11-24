from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_event_subscription import RDSEventSubscription


class RDSDescribeEventSubscriptionsResponse(BaseModel):
    Marker: StrictStr | None = None
    EventSubscriptionsList: list[RDSEventSubscription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
