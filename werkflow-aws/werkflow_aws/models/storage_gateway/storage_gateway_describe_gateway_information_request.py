from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeGatewayInformationRequest(BaseModel):
    GatewayARN: StrictStr
