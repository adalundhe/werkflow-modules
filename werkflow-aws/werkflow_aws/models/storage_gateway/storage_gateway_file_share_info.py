from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayFileShareInfo(BaseModel):
    FileShareType: StrictStr | None = None
    FileShareARN: StrictStr | None = None
    FileShareId: StrictStr | None = None
    FileShareStatus: StrictStr | None = None
    GatewayARN: StrictStr | None = None
