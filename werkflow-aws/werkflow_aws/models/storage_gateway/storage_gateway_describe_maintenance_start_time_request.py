from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeMaintenanceStartTimeRequest(BaseModel):
    GatewayARN: StrictStr
