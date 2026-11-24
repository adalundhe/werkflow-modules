from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableImageDeregistrationProtectionRequest(BaseModel):
    ImageId: StrictStr
    WithCooldown: StrictBool | None = None
    DryRun: StrictBool | None = None
