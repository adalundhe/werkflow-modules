from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectUpdateLagRequest(BaseModel):
    lagId: StrictStr
    lagName: StrictStr | None = None
    minimumLinks: StrictInt | None = None
    encryptionMode: StrictStr | None = None
