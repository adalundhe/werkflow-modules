from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_db_event_subscription import DocumentDBEventSubscription


class DocumentDBCreateEventSubscriptionResponse(BaseModel):
    EventSubscription: DocumentDBEventSubscription | None = None
    ResponseMetadata: dict[str, Any] | None = None
