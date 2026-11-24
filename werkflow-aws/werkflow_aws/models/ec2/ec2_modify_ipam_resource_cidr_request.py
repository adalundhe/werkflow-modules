from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyIpamResourceCidrRequest(BaseModel):
    ResourceId: StrictStr
    ResourceCidr: StrictStr
    ResourceRegion: StrictStr
    CurrentIpamScopeId: StrictStr
    Monitored: StrictBool
    DryRun: StrictBool | None = None
    DestinationIpamScopeId: StrictStr | None = None
