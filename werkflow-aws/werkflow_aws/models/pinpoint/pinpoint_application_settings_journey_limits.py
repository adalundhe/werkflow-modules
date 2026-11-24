from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .pinpoint_journey_timeframe_cap import PinpointJourneyTimeframeCap


class PinpointApplicationSettingsJourneyLimits(BaseModel):
    DailyCap: StrictInt | None = None
    TimeframeCap: PinpointJourneyTimeframeCap | None = None
    TotalCap: StrictInt | None = None
