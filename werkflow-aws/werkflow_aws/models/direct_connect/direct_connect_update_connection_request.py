from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectUpdateConnectionRequest(BaseModel):
    connectionId: StrictStr
    connectionName: StrictStr | None = None
    encryptionMode: StrictStr | None = None
