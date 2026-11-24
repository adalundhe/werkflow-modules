from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_coip_pool import EC2CoipPool


class EC2DescribeCoipPoolsResponse(BaseModel):
    CoipPools: list[EC2CoipPool] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
