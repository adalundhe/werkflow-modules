from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisassociateIpamResourceDiscoveryRequest(BaseModel):
    IpamResourceDiscoveryAssociationId: StrictStr
    DryRun: StrictBool | None = None
