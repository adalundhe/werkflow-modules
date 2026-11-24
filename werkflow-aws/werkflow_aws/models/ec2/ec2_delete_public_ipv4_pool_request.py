from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeletePublicIpv4PoolRequest(BaseModel):
    PoolId: StrictStr
    DryRun: StrictBool | None = None
    NetworkBorderGroup: StrictStr | None = None
