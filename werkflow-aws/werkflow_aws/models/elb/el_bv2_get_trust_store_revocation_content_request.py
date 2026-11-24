from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2GetTrustStoreRevocationContentRequest(BaseModel):
    TrustStoreArn: StrictStr
    RevocationId: StrictInt
