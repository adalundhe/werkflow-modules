from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2RemoveTrustStoreRevocationsRequest(BaseModel):
    TrustStoreArn: StrictStr
    RevocationIds: list[StrictInt]
