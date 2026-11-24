from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteCoipPoolRequest(BaseModel):
    CoipPoolId: StrictStr
    DryRun: StrictBool | None = None
