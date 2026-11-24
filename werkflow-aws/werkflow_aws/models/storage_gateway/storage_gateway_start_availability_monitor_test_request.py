from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayStartAvailabilityMonitorTestRequest(BaseModel):
    GatewayARN: StrictStr
