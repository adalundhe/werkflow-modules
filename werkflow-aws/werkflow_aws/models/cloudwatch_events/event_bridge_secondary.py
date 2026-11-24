from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeSecondary(BaseModel):
    Route: StrictStr | None = None
