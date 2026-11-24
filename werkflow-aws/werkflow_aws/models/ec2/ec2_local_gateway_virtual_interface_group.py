from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2LocalGatewayVirtualInterfaceGroup(BaseModel):
    LocalGatewayVirtualInterfaceGroupId: StrictStr | None = None
    LocalGatewayVirtualInterfaceIds: list[StrictStr] | None = None
    LocalGatewayId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    LocalBgpAsn: StrictInt | None = None
    LocalBgpAsnExtended: StrictInt | None = None
    LocalGatewayVirtualInterfaceGroupArn: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    ConfigurationState: StrictStr | None = None
