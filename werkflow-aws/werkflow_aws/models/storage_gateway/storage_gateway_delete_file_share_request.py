from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class StorageGatewayDeleteFileShareRequest(BaseModel):
    FileShareARN: StrictStr
    ForceDelete: StrictBool | None = None
