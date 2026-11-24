from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_write_segment_request import PinpointWriteSegmentRequest


class PinpointCreateSegmentRequest(BaseModel):
    ApplicationId: StrictStr
    WriteSegmentRequest: PinpointWriteSegmentRequest
