from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_peering_connection_options_request import EC2PeeringConnectionOptionsRequest


class EC2ModifyVpcPeeringConnectionOptionsRequest(BaseModel):
    VpcPeeringConnectionId: StrictStr
    AccepterPeeringConnectionOptions: EC2PeeringConnectionOptionsRequest | None = None
    DryRun: StrictBool | None = None
    RequesterPeeringConnectionOptions: EC2PeeringConnectionOptionsRequest | None = None
