from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PeeringTgwInfo(BaseModel):
    TransitGatewayId: StrictStr | None = None
    CoreNetworkId: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Region: StrictStr | None = None
