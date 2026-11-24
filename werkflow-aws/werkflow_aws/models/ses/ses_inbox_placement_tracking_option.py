from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SESInboxPlacementTrackingOption(BaseModel):
    Global: StrictBool | None = None
    TrackedIsps: list[StrictStr] | None = None
