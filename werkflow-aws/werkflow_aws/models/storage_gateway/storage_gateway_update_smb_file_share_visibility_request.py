from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class StorageGatewayUpdateSMBFileShareVisibilityRequest(BaseModel):
    GatewayARN: StrictStr
    FileSharesVisible: StrictBool
