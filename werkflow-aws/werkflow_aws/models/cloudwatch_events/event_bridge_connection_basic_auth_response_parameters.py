from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeConnectionBasicAuthResponseParameters(BaseModel):
    Username: StrictStr | None = None
