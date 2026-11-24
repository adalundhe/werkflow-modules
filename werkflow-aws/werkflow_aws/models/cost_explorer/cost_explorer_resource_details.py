from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_ec2_resource_details import CostExplorerEC2ResourceDetails


class CostExplorerResourceDetails(BaseModel):
    EC2ResourceDetails: CostExplorerEC2ResourceDetails | None = None
