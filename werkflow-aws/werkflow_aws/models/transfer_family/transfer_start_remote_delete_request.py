from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferStartRemoteDeleteRequest(BaseModel):
    ConnectorId: StrictStr
    DeletePath: StrictStr
