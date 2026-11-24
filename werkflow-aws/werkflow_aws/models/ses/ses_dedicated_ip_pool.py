from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDedicatedIpPool(BaseModel):
    PoolName: StrictStr | None = None
    ScalingMode: StrictStr | None = None
