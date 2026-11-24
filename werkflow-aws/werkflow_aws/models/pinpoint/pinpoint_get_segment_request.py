from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetSegmentRequest(BaseModel):
    ApplicationId: StrictStr
    SegmentId: StrictStr
