from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetSegmentVersionRequest(BaseModel):
    ApplicationId: StrictStr
    SegmentId: StrictStr
    Version: StrictStr
