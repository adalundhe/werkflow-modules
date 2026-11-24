from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .pinpoint_journey_timeframe_cap import PinpointJourneyTimeframeCap


class PinpointJourneyLimits(BaseModel):
    DailyCap: StrictInt | None = None
    EndpointReentryCap: StrictInt | None = None
    MessagesPerSecond: StrictInt | None = None
    EndpointReentryInterval: StrictStr | None = None
    TimeframeCap: PinpointJourneyTimeframeCap | None = None
    TotalCap: StrictInt | None = None
