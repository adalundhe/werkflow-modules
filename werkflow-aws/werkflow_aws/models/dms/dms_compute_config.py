from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSComputeConfig(BaseModel):
    AvailabilityZone: StrictStr | None = None
    DnsNameServers: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    MaxCapacityUnits: StrictInt | None = None
    MinCapacityUnits: StrictInt | None = None
    MultiAZ: StrictBool | None = None
    PreferredMaintenanceWindow: StrictStr | None = None
    ReplicationSubnetGroupId: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
