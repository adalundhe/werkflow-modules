from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RdsCustomClusterConfiguration(BaseModel):
    InterconnectSubnetId: StrictStr | None = None
    TransitGatewayMulticastDomainId: StrictStr | None = None
    ReplicaMode: StrictStr | None = None
