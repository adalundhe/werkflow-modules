from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ReleaseAddressRequest(BaseModel):
    AllocationId: StrictStr | None = None
    PublicIp: StrictStr | None = None
    NetworkBorderGroup: StrictStr | None = None
    DryRun: StrictBool | None = None
