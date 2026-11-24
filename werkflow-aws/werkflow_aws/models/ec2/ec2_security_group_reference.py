from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SecurityGroupReference(BaseModel):
    GroupId: StrictStr | None = None
    ReferencingVpcId: StrictStr | None = None
    VpcPeeringConnectionId: StrictStr | None = None
    TransitGatewayId: StrictStr | None = None
