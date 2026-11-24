from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2WithdrawByoipCidrRequest(BaseModel):
    Cidr: StrictStr
    DryRun: StrictBool | None = None
