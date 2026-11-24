from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KinesisWarmThroughputObject(BaseModel):
    TargetMiBps: StrictInt | None = None
    CurrentMiBps: StrictInt | None = None
