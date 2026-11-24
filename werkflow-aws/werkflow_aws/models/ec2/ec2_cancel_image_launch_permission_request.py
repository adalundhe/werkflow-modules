from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CancelImageLaunchPermissionRequest(BaseModel):
    ImageId: StrictStr
    DryRun: StrictBool | None = None
