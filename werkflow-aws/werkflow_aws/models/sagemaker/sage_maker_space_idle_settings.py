from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerSpaceIdleSettings(BaseModel):
    IdleTimeoutInMinutes: StrictInt | None = None
