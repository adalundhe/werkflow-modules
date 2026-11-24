from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteDeliverySourceRequest(BaseModel):
    name: StrictStr
