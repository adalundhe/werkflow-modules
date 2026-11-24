from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableIpamInternetRegistryAssociationRequest(BaseModel):
    IpamInternetRegistryAssociationId: StrictStr
    RpkiVersion: StrictStr
    ServiceUri: StrictStr
    ChildHandle: StrictStr
    ParentHandle: StrictStr
    ParentBpkiTa: StrictStr
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
