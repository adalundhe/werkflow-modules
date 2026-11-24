from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class StorageGatewayRefreshCacheRequest(BaseModel):
    FileShareARN: StrictStr
    FolderList: list[StrictStr] | None = None
    Recursive: StrictBool | None = None
