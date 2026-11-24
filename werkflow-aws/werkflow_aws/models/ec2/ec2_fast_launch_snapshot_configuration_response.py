from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2FastLaunchSnapshotConfigurationResponse(BaseModel):
    TargetResourceCount: StrictInt | None = None
