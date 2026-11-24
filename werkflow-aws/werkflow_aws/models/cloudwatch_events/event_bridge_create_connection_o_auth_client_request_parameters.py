from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeCreateConnectionOAuthClientRequestParameters(BaseModel):
    ClientID: StrictStr
    ClientSecret: StrictStr
