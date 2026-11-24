from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteEventStreamRequest(BaseModel):
    ApplicationId: StrictStr
