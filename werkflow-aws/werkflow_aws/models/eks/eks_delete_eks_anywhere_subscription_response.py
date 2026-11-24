from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .eks_anywhere_subscription import EksAnywhereSubscription


class EKSDeleteEksAnywhereSubscriptionResponse(BaseModel):
    subscription: EksAnywhereSubscription | None = None
    ResponseMetadata: dict[str, Any] | None = None
