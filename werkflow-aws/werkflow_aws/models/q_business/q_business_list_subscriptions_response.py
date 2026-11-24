from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_subscription import QBusinessSubscription


class QBusinessListSubscriptionsResponse(BaseModel):
    nextToken: StrictStr | None = None
    subscriptions: list[QBusinessSubscription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
