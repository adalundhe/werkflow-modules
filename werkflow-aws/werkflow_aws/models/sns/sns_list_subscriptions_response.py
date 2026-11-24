from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sns_subscription import SNSSubscription


class SNSListSubscriptionsResponse(BaseModel):
    Subscriptions: list[SNSSubscription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
