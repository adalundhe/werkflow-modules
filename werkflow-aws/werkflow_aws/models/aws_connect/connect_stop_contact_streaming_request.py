from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectStopContactStreamingRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    StreamingId: StrictStr
