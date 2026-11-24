from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2AssociateTrunkInterfaceRequest(BaseModel):
    BranchInterfaceId: StrictStr
    TrunkInterfaceId: StrictStr
    VlanId: StrictInt | None = None
    GreKey: StrictInt | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
