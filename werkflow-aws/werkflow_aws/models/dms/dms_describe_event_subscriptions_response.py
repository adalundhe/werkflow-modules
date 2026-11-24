from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_event_subscription import DMSEventSubscription


class DMSDescribeEventSubscriptionsResponse(BaseModel):
    Marker: StrictStr | None = None
    EventSubscriptionsList: list[DMSEventSubscription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
