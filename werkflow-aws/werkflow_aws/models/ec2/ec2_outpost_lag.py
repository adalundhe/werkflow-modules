from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2OutpostLag(BaseModel):
    OutpostArn: StrictStr | None = None
    OwnerId: StrictStr | None = None
    State: StrictStr | None = None
    OutpostLagId: StrictStr | None = None
    LocalGatewayVirtualInterfaceIds: list[StrictStr] | None = None
    ServiceLinkVirtualInterfaceIds: list[StrictStr] | None = None
    Tags: list[EC2TagModel] | None = None
