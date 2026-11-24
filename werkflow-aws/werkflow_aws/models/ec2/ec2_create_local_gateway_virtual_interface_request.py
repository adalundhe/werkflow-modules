from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateLocalGatewayVirtualInterfaceRequest(BaseModel):
    LocalGatewayVirtualInterfaceGroupId: StrictStr
    OutpostLagId: StrictStr
    Vlan: StrictInt
    LocalAddress: StrictStr
    PeerAddress: StrictStr
    PeerBgpAsn: StrictInt | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
    PeerBgpAsnExtended: StrictInt | None = None
