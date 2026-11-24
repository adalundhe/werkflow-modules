from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EC2FastLaunchSnapshotConfigurationRequest(BaseModel):
    TargetResourceCount: StrictInt | None = None
