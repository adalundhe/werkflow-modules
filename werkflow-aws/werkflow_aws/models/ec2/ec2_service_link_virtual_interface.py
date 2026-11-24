from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2ServiceLinkVirtualInterface(BaseModel):
    ServiceLinkVirtualInterfaceId: StrictStr | None = None
    ServiceLinkVirtualInterfaceArn: StrictStr | None = None
    OutpostId: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    OwnerId: StrictStr | None = None
    LocalAddress: StrictStr | None = None
    PeerAddress: StrictStr | None = None
    PeerBgpAsn: StrictInt | None = None
    Vlan: StrictInt | None = None
    OutpostLagId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    ConfigurationState: StrictStr | None = None
