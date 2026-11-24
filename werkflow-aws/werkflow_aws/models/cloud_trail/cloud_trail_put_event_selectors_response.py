from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_advanced_event_selector import CloudTrailAdvancedEventSelector
from .cloud_trail_event_selector import CloudTrailEventSelector


class CloudTrailPutEventSelectorsResponse(BaseModel):
    TrailARN: StrictStr | None = None
    EventSelectors: list[CloudTrailEventSelector] | None = None
    AdvancedEventSelectors: list[CloudTrailAdvancedEventSelector] | None = None
    ResponseMetadata: dict[str, Any] | None = None
