from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVolumeRequest(BaseModel):
    VolumeId: StrictStr
    DryRun: StrictBool | None = None
