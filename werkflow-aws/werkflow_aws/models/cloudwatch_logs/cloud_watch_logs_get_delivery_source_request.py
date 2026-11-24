from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGetDeliverySourceRequest(BaseModel):
    name: StrictStr
