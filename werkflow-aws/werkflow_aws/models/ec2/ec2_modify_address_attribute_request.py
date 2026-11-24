from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyAddressAttributeRequest(BaseModel):
    AllocationId: StrictStr
    DomainName: StrictStr | None = None
    DryRun: StrictBool | None = None
