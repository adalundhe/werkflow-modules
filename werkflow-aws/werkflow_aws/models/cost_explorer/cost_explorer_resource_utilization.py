from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_ec2_resource_utilization import CostExplorerEC2ResourceUtilization


class CostExplorerResourceUtilization(BaseModel):
    EC2ResourceUtilization: CostExplorerEC2ResourceUtilization | None = None
