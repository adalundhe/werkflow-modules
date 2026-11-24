from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_event_subscription import RedshiftEventSubscription


class RedshiftModifyEventSubscriptionResponse(BaseModel):
    EventSubscription: RedshiftEventSubscription | None = None
    ResponseMetadata: dict[str, Any] | None = None
