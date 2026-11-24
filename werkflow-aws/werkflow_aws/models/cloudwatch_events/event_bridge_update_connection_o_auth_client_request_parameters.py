from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeUpdateConnectionOAuthClientRequestParameters(BaseModel):
    ClientID: StrictStr | None = None
    ClientSecret: StrictStr | None = None
