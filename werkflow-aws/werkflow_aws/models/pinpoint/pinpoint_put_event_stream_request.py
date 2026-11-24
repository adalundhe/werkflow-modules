from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_write_event_stream import PinpointWriteEventStream


class PinpointPutEventStreamRequest(BaseModel):
    ApplicationId: StrictStr
    WriteEventStream: PinpointWriteEventStream
