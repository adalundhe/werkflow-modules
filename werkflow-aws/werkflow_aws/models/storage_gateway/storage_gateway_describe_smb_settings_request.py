from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeSMBSettingsRequest(BaseModel):
    GatewayARN: StrictStr
