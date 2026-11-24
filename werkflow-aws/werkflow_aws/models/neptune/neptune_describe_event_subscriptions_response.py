from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_event_subscription import NeptuneEventSubscription


class NeptuneDescribeEventSubscriptionsResponse(BaseModel):
    Marker: StrictStr | None = None
    EventSubscriptionsList: list[NeptuneEventSubscription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
