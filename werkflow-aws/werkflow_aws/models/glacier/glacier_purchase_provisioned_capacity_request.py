from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierPurchaseProvisionedCapacityRequest(BaseModel):
    accountId: StrictStr
