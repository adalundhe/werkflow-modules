from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_reserved_instances import EC2ReservedInstances


class EC2DescribeReservedInstancesResponse(BaseModel):
    ReservedInstances: list[EC2ReservedInstances] | None = None
    ResponseMetadata: dict[str, Any] | None = None
