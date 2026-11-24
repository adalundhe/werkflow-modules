from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteTrafficMirrorTargetRequest(BaseModel):
    TrafficMirrorTargetId: StrictStr
    DryRun: StrictBool | None = None
