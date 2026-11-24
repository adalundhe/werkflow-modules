from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class StorageGatewayEvictFilesFailingUploadRequest(BaseModel):
    FileShareARN: StrictStr
    ForceRemove: StrictBool | None = None
