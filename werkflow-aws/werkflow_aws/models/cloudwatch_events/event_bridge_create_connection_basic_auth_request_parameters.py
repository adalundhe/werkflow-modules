from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeCreateConnectionBasicAuthRequestParameters(BaseModel):
    Username: StrictStr
    Password: StrictStr
