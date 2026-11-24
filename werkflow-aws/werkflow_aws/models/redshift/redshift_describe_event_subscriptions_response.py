from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_event_subscription import RedshiftEventSubscription


class RedshiftDescribeEventSubscriptionsResponse(BaseModel):
    Marker: StrictStr | None = None
    EventSubscriptionsList: list[RedshiftEventSubscription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
