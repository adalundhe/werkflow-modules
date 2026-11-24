from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AttachVolumeRequest(BaseModel):
    Device: StrictStr
    InstanceId: StrictStr
    VolumeId: StrictStr
    DryRun: StrictBool | None = None
