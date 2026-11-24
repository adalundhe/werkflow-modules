from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetDeliveryDestinationPolicyRequest(BaseModel):
    deliveryDestinationName: StrictStr
