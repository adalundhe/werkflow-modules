from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2RevokeClientVpnIngressRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    TargetNetworkCidr: StrictStr
    AccessGroupId: StrictStr | None = None
    RevokeAllGroups: StrictBool | None = None
    DryRun: StrictBool | None = None
