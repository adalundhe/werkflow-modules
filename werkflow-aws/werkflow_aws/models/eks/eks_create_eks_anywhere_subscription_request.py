from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .eks_anywhere_subscription_term import EksAnywhereSubscriptionTerm


class EKSCreateEksAnywhereSubscriptionRequest(BaseModel):
    name: StrictStr
    term: EksAnywhereSubscriptionTerm
    licenseQuantity: StrictInt | None = None
    licenseType: Literal['Cluster'] | None = None
    autoRenew: StrictBool | None = None
    clientRequestToken: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
