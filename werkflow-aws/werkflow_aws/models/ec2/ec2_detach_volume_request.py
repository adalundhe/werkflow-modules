from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DetachVolumeRequest(BaseModel):
    VolumeId: StrictStr
    Device: StrictStr | None = None
    Force: StrictBool | None = None
    InstanceId: StrictStr | None = None
    DryRun: StrictBool | None = None
