from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetDeliveryRequest(BaseModel):
    id: StrictStr
