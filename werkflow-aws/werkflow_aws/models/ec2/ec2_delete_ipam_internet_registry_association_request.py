from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteIpamInternetRegistryAssociationRequest(BaseModel):
    IpamInternetRegistryAssociationId: StrictStr
    DryRun: StrictBool | None = None
