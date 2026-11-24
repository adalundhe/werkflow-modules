from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_replica_mode import RDSReplicaMode


class RDSRdsCustomClusterConfiguration(BaseModel):
    InterconnectSubnetId: StrictStr | None = None
    TransitGatewayMulticastDomainId: StrictStr | None = None
    ReplicaMode: RDSReplicaMode | None = None
