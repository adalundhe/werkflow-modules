from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayNotifyWhenUploadedRequest(BaseModel):
    FileShareARN: StrictStr
