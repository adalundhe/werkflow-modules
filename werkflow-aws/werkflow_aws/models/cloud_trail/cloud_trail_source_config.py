from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .cloud_trail_advanced_event_selector import CloudTrailAdvancedEventSelector


class CloudTrailSourceConfig(BaseModel):
    ApplyToAllRegions: StrictBool | None = None
    AdvancedEventSelectors: list[CloudTrailAdvancedEventSelector] | None = None
