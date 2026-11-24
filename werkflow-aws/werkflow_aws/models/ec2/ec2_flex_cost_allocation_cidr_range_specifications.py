from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_flex_cost_allocation_cidr_mapping import EC2FlexCostAllocationCidrMapping


class EC2FlexCostAllocationCidrRangeSpecifications(BaseModel):
    PrefixesType: StrictStr | None = None
    Prefixes: list[EC2FlexCostAllocationCidrMapping] | None = None
