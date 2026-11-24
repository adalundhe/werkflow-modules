from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ResetNetworkInterfaceAttributeRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    DryRun: StrictBool | None = None
    SourceDestCheck: StrictStr | None = None
