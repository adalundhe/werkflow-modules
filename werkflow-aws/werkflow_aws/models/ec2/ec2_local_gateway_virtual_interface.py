from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2LocalGatewayVirtualInterface(BaseModel):
    LocalGatewayVirtualInterfaceId: StrictStr | None = None
    LocalGatewayId: StrictStr | None = None
    LocalGatewayVirtualInterfaceGroupId: StrictStr | None = None
    LocalGatewayVirtualInterfaceArn: StrictStr | None = None
    OutpostLagId: StrictStr | None = None
    Vlan: StrictInt | None = None
    LocalAddress: StrictStr | None = None
    PeerAddress: StrictStr | None = None
    LocalBgpAsn: StrictInt | None = None
    PeerBgpAsn: StrictInt | None = None
    PeerBgpAsnExtended: StrictInt | None = None
    OwnerId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    ConfigurationState: StrictStr | None = None
