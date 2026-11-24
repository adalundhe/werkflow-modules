from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDeleteAccessRequest(BaseModel):
    ServerId: StrictStr
    ExternalId: StrictStr
