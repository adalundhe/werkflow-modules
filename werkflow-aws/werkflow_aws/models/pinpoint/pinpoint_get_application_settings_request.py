from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetApplicationSettingsRequest(BaseModel):
    ApplicationId: StrictStr
