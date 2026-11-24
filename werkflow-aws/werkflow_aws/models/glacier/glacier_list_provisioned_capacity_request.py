from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierListProvisionedCapacityRequest(BaseModel):
    accountId: StrictStr
