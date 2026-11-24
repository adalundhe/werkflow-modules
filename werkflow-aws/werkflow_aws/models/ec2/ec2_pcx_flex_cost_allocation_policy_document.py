from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_flex_cost_allocation_cidr_range_specifications import EC2FlexCostAllocationCidrRangeSpecifications


class EC2PcxFlexCostAllocationPolicyDocument(BaseModel):
    ReportingGranularity: list[StrictStr] | None = None
    Dimensions: list[StrictStr] | None = None
    CidrRangeSpecifications: EC2FlexCostAllocationCidrRangeSpecifications | None = None
