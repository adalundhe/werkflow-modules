from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_db_event_subscription import DocumentDBEventSubscription


class DocumentDBDescribeEventSubscriptionsResponse(BaseModel):
    Marker: StrictStr | None = None
    EventSubscriptionsList: list[DocumentDBEventSubscription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
