from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableAddressTransferRequest(BaseModel):
    AllocationId: StrictStr
    TransferAccountId: StrictStr
    DryRun: StrictBool | None = None
