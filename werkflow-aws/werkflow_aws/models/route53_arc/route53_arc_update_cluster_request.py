from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53ARCUpdateClusterRequest(BaseModel):
    ClusterArn: StrictStr
    NetworkType: Literal['IPV4', 'DUALSTACK']
