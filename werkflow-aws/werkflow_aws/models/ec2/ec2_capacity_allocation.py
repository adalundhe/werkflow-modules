from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_capacity_allocation_metadata_entry import EC2CapacityAllocationMetadataEntry


class EC2CapacityAllocation(BaseModel):
    AllocationType: StrictStr | None = None
    Count: StrictInt | None = None
    AllocationMetadata: list[EC2CapacityAllocationMetadataEntry] | None = None
