from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_ec2_specification import CostExplorerEC2Specification


class CostExplorerServiceSpecification(BaseModel):
    EC2Specification: CostExplorerEC2Specification | None = None
