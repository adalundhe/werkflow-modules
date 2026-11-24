from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetDeliveryDestinationRequest(BaseModel):
    name: StrictStr
