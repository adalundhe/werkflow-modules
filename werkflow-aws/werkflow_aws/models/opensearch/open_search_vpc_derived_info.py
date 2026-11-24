from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchVPCDerivedInfo(BaseModel):
    VPCId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    AvailabilityZones: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    EgressEnabled: StrictBool | None = None
