from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CreateCoipCidrRequest(BaseModel):
    Cidr: StrictStr
    CoipPoolId: StrictStr
    DryRun: StrictBool | None = None
