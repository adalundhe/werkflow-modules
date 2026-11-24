from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_capacity_block_status import EC2CapacityBlockStatus


class EC2DescribeCapacityBlockStatusResponse(BaseModel):
    CapacityBlockStatuses: list[EC2CapacityBlockStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
