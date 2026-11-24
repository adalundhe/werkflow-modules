from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteDeliveryDestinationPolicyRequest(BaseModel):
    deliveryDestinationName: StrictStr
