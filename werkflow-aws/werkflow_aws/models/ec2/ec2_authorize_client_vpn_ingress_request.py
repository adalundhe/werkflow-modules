from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AuthorizeClientVpnIngressRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    TargetNetworkCidr: StrictStr
    AccessGroupId: StrictStr | None = None
    AuthorizeAllGroups: StrictBool | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
