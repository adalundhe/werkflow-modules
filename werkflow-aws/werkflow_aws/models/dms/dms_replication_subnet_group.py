from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_subnet import DMSSubnet


class DMSReplicationSubnetGroup(BaseModel):
    ReplicationSubnetGroupIdentifier: StrictStr | None = None
    ReplicationSubnetGroupDescription: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetGroupStatus: StrictStr | None = None
    Subnets: list[DMSSubnet] | None = None
    SupportedNetworkTypes: list[StrictStr] | None = None
    IsReadOnly: StrictBool | None = None
