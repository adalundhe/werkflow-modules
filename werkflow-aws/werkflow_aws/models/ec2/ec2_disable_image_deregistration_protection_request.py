from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisableImageDeregistrationProtectionRequest(BaseModel):
    ImageId: StrictStr
    DryRun: StrictBool | None = None
