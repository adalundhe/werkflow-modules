from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteSegmentRequest(BaseModel):
    ApplicationId: StrictStr
    SegmentId: StrictStr
