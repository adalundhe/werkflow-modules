from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKCreateVpcConnectionRequest(BaseModel):
    TargetClusterArn: StrictStr
    Authentication: StrictStr
    VpcId: StrictStr
    ClientSubnets: list[StrictStr]
    SecurityGroups: list[StrictStr]
    Tags: dict[StrictStr, StrictStr] | None = None
