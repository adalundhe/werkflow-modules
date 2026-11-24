from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateLocalGatewayVirtualInterfaceGroupRequest(BaseModel):
    LocalGatewayId: StrictStr
    LocalBgpAsn: StrictInt | None = None
    LocalBgpAsnExtended: StrictInt | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
