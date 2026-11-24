from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2RestoreAddressToClassicRequest(BaseModel):
    PublicIp: StrictStr
    DryRun: StrictBool | None = None
