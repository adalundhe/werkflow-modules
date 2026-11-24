from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteTrafficMirrorSessionRequest(BaseModel):
    TrafficMirrorSessionId: StrictStr
    DryRun: StrictBool | None = None
