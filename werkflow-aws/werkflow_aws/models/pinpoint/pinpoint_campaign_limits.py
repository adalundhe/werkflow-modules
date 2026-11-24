from __future__ import annotations
from pydantic import BaseModel, StrictInt


class PinpointCampaignLimits(BaseModel):
    Daily: StrictInt | None = None
    MaximumDuration: StrictInt | None = None
    MessagesPerSecond: StrictInt | None = None
    Total: StrictInt | None = None
    Session: StrictInt | None = None
