from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_subscription_details import QBusinessSubscriptionDetails


class QBusinessUpdateSubscriptionResponse(BaseModel):
    subscriptionArn: StrictStr | None = None
    currentSubscription: QBusinessSubscriptionDetails | None = None
    nextSubscription: QBusinessSubscriptionDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
