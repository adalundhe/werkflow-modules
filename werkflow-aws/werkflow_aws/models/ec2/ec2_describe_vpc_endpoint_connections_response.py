from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpc_endpoint_connection import EC2VpcEndpointConnection


class EC2DescribeVpcEndpointConnectionsResponse(BaseModel):
    VpcEndpointConnections: list[EC2VpcEndpointConnection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
