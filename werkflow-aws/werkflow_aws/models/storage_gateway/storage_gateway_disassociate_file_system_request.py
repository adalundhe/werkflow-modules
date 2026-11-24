from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class StorageGatewayDisassociateFileSystemRequest(BaseModel):
    FileSystemAssociationARN: StrictStr
    ForceDelete: StrictBool | None = None
