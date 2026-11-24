from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_vpc_peering_connection import EC2VpcPeeringConnection


class EC2CreateVpcPeeringConnectionResponse(BaseModel):
    VpcPeeringConnection: EC2VpcPeeringConnection | None = None
    ResponseMetadata: dict[str, Any] | None = None
