from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2LocalGatewayRouteTableVirtualInterfaceGroupAssociation(BaseModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: StrictStr | None = None
    LocalGatewayVirtualInterfaceGroupId: StrictStr | None = None
    LocalGatewayId: StrictStr | None = None
    LocalGatewayRouteTableId: StrictStr | None = None
    LocalGatewayRouteTableArn: StrictStr | None = None
    OwnerId: StrictStr | None = None
    State: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
