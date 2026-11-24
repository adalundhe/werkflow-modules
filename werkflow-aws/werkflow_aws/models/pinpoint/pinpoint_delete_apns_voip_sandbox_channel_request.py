from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteApnsVoipSandboxChannelRequest(BaseModel):
    ApplicationId: StrictStr
