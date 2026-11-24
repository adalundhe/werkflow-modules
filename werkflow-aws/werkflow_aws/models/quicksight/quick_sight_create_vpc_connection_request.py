from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_tag import QuickSightTag


class QuickSightCreateVPCConnectionRequest(BaseModel):
    AwsAccountId: StrictStr
    VPCConnectionId: StrictStr
    Name: StrictStr
    SubnetIds: list[StrictStr]
    SecurityGroupIds: list[StrictStr]
    RoleArn: StrictStr
    DnsResolvers: list[StrictStr] | None = None
    Tags: list[QuickSightTag] | None = None
