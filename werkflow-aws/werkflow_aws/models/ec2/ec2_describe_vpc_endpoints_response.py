from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpc_endpoint import EC2VpcEndpoint


class EC2DescribeVpcEndpointsResponse(BaseModel):
    VpcEndpoints: list[EC2VpcEndpoint] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
