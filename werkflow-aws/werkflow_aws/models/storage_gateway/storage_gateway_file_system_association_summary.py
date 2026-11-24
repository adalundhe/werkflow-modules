from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayFileSystemAssociationSummary(BaseModel):
    FileSystemAssociationId: StrictStr | None = None
    FileSystemAssociationARN: StrictStr | None = None
    FileSystemAssociationStatus: StrictStr | None = None
    GatewayARN: StrictStr | None = None
