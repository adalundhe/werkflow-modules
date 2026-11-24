from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CloudWatchMetricCharacteristics(BaseModel):
    PeriodicSpikes: StrictBool | None = None
