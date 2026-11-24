from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeFileSystemAssociationsRequest(BaseModel):
    FileSystemAssociationARNList: list[StrictStr]
