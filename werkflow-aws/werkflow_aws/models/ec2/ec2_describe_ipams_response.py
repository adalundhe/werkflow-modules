from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam import EC2Ipam


class EC2DescribeIpamsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Ipams: list[EC2Ipam] | None = None
    ResponseMetadata: dict[str, Any] | None = None
