from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDisassociateMacSecKeyRequest(BaseModel):
    connectionId: StrictStr
    secretARN: StrictStr
