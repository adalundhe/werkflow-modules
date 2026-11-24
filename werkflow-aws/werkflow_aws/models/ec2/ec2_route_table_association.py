from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_route_table_association_state import EC2RouteTableAssociationState


class EC2RouteTableAssociation(BaseModel):
    Main: StrictBool | None = None
    RouteTableAssociationId: StrictStr | None = None
    RouteTableId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    GatewayId: StrictStr | None = None
    PublicIpv4Pool: StrictStr | None = None
    AssociationState: EC2RouteTableAssociationState | None = None
