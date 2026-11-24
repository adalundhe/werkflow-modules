from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ApplySecurityGroupsToClientVpnTargetNetworkRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    VpcId: StrictStr
    SecurityGroupIds: list[StrictStr]
    DryRun: StrictBool | None = None
