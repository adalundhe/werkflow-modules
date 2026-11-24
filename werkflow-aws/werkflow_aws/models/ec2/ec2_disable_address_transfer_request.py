from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisableAddressTransferRequest(BaseModel):
    AllocationId: StrictStr
    DryRun: StrictBool | None = None
