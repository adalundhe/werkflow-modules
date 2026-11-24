from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetInAppMessagesRequest(BaseModel):
    ApplicationId: StrictStr
    EndpointId: StrictStr
