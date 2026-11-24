from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteDeliveryDestinationRequest(BaseModel):
    name: StrictStr
