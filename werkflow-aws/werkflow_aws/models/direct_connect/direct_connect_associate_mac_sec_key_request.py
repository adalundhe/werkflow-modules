from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectAssociateMacSecKeyRequest(BaseModel):
    connectionId: StrictStr
    secretARN: StrictStr | None = None
    ckn: StrictStr | None = None
    cak: StrictStr | None = None
