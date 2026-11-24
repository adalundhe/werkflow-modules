from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUpdateVPCConnectionRequest(BaseModel):
    AwsAccountId: StrictStr
    VPCConnectionId: StrictStr
    Name: StrictStr
    SubnetIds: list[StrictStr]
    SecurityGroupIds: list[StrictStr]
    RoleArn: StrictStr
    DnsResolvers: list[StrictStr] | None = None
