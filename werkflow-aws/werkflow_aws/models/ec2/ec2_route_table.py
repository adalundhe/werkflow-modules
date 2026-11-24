from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_propagating_vgw import EC2PropagatingVgw
from .ec2_route import EC2Route
from .ec2_route_table_association import EC2RouteTableAssociation
from .ec2_tag_model import EC2TagModel


class EC2RouteTable(BaseModel):
    Associations: list[EC2RouteTableAssociation] | None = None
    PropagatingVgws: list[EC2PropagatingVgw] | None = None
    RouteTableId: StrictStr | None = None
    Routes: list[EC2Route] | None = None
    Tags: list[EC2TagModel] | None = None
    VpcId: StrictStr | None = None
    OwnerId: StrictStr | None = None
