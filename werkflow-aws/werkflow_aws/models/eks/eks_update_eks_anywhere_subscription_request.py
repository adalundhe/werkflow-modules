from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EKSUpdateEksAnywhereSubscriptionRequest(BaseModel):
    id: StrictStr
    autoRenew: StrictBool
    clientRequestToken: StrictStr | None = None
