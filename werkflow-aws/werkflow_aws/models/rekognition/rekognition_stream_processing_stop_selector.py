from __future__ import annotations
from pydantic import BaseModel, StrictInt


class RekognitionStreamProcessingStopSelector(BaseModel):
    MaxDurationInSeconds: StrictInt | None = None
