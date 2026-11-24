from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeConnectionOAuthClientResponseParameters(BaseModel):
    ClientID: StrictStr | None = None
