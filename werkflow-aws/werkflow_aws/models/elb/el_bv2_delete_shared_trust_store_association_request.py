from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2DeleteSharedTrustStoreAssociationRequest(BaseModel):
    TrustStoreArn: StrictStr
    ResourceArn: StrictStr
