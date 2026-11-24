from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsPutDeliveryDestinationPolicyRequest(BaseModel):
    deliveryDestinationName: StrictStr
    deliveryDestinationPolicy: StrictStr
