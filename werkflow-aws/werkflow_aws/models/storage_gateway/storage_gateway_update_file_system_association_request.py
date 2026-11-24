from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_cache_attributes import StorageGatewayCacheAttributes


class StorageGatewayUpdateFileSystemAssociationRequest(BaseModel):
    FileSystemAssociationARN: StrictStr
    UserName: StrictStr | None = None
    Password: StrictStr | None = None
    AuditDestinationARN: StrictStr | None = None
    CacheAttributes: StorageGatewayCacheAttributes | None = None
