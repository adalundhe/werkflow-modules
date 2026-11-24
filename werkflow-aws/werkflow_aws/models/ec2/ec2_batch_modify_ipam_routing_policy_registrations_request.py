from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2BatchModifyIpamRoutingPolicyRegistrationsRequest(BaseModel):
    IpamInternetRegistryAssociationId: StrictStr
    DeltaJson: StrictStr
    DryRun: StrictBool | None = None
    Force: StrictBool | None = None
    ClientToken: StrictStr | None = None
