from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayFileSystemAssociationStatusDetail(BaseModel):
    ErrorCode: StrictStr | None = None
