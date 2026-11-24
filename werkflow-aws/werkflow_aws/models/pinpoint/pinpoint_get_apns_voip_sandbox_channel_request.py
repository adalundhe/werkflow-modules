from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetApnsVoipSandboxChannelRequest(BaseModel):
    ApplicationId: StrictStr
