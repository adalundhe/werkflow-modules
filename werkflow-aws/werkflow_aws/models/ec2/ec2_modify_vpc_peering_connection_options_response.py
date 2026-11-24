from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_peering_connection_options import EC2PeeringConnectionOptions


class EC2ModifyVpcPeeringConnectionOptionsResponse(BaseModel):
    AccepterPeeringConnectionOptions: EC2PeeringConnectionOptions | None = None
    RequesterPeeringConnectionOptions: EC2PeeringConnectionOptions | None = None
    ResponseMetadata: dict[str, Any] | None = None
