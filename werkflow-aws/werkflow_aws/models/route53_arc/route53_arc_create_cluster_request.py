from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53ARCCreateClusterRequest(BaseModel):
    ClusterName: StrictStr
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    NetworkType: Literal['IPV4', 'DUALSTACK'] | None = None
