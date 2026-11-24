from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_anywhere_subscription import EksAnywhereSubscription


class EKSListEksAnywhereSubscriptionsResponse(BaseModel):
    subscriptions: list[EksAnywhereSubscription] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
