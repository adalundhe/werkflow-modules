from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_rebalancing import MSKRebalancing


class MSKUpdateRebalancingRequest(BaseModel):
    ClusterArn: StrictStr
    CurrentVersion: StrictStr
    Rebalancing: MSKRebalancing
