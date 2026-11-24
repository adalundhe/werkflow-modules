from __future__ import annotations
from pydantic import BaseModel, StrictInt


class PinpointJourneyTimeframeCap(BaseModel):
    Cap: StrictInt | None = None
    Days: StrictInt | None = None
