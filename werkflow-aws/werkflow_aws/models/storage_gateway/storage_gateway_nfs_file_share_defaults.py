from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayNFSFileShareDefaults(BaseModel):
    FileMode: StrictStr | None = None
    DirectoryMode: StrictStr | None = None
    GroupId: StrictInt | None = None
    OwnerId: StrictInt | None = None
