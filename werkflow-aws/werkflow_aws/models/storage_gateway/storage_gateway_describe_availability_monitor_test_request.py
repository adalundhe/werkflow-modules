from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeAvailabilityMonitorTestRequest(BaseModel):
    GatewayARN: StrictStr
