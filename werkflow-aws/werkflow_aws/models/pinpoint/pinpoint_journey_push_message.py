from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointJourneyPushMessage(BaseModel):
    TimeToLive: StrictStr | None = None
