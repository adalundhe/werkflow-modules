from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_block import EC2CapacityBlock


class EC2DescribeCapacityBlocksResponse(BaseModel):
    CapacityBlocks: list[EC2CapacityBlock] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
