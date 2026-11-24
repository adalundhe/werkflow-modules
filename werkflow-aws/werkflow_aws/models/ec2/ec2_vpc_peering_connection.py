from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_vpc_peering_connection_state_reason import EC2VpcPeeringConnectionStateReason
from .ec2_vpc_peering_connection_vpc_info import EC2VpcPeeringConnectionVpcInfo


class EC2VpcPeeringConnection(BaseModel):
    AccepterVpcInfo: EC2VpcPeeringConnectionVpcInfo | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
    RequesterVpcInfo: EC2VpcPeeringConnectionVpcInfo | None = None
    Status: EC2VpcPeeringConnectionStateReason | None = None
    Tags: list[EC2TagModel] | None = None
    VpcPeeringConnectionId: StrictStr | None = None
    MultipathResilienceStatus: StrictStr | None = None
