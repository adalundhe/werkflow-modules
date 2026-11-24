from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetAppRequest(BaseModel):
    ApplicationId: StrictStr
