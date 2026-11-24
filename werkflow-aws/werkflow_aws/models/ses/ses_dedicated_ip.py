from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SESDedicatedIp(BaseModel):
    Ip: StrictStr | None = None
    WarmupStatus: StrictStr | None = None
    WarmupPercentage: StrictInt | None = None
    PoolName: StrictStr | None = None
