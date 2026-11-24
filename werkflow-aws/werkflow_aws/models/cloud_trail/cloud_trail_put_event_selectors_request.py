from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_trail_advanced_event_selector import CloudTrailAdvancedEventSelector
from .cloud_trail_event_selector import CloudTrailEventSelector


class CloudTrailPutEventSelectorsRequest(BaseModel):
    TrailName: StrictStr
    EventSelectors: list[CloudTrailEventSelector] | None = None
    AdvancedEventSelectors: list[CloudTrailAdvancedEventSelector] | None = None
