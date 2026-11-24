from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_create_peering_connection_options_request import EC2CreatePeeringConnectionOptionsRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateVpcPeeringConnectionRequest(BaseModel):
    VpcId: StrictStr
    PeerRegion: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    RequesterPeeringConnectionOptions: EC2CreatePeeringConnectionOptionsRequest | None = None
    DryRun: StrictBool | None = None
    PeerVpcId: StrictStr | None = None
    PeerOwnerId: StrictStr | None = None
