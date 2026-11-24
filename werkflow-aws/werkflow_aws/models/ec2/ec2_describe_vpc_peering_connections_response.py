from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpc_peering_connection import EC2VpcPeeringConnection


class EC2DescribeVpcPeeringConnectionsResponse(BaseModel):
    VpcPeeringConnections: list[EC2VpcPeeringConnection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
