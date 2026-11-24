from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .lightsail_auto_snapshot_add_on_request import LightsailAutoSnapshotAddOnRequest
from .lightsail_stop_instance_on_idle_request import LightsailStopInstanceOnIdleRequest


class LightsailAddOnRequest(BaseModel):
    addOnType: Literal['AutoSnapshot', 'StopInstanceOnIdle']
    autoSnapshotAddOnRequest: LightsailAutoSnapshotAddOnRequest | None = None
    stopInstanceOnIdleRequest: LightsailStopInstanceOnIdleRequest | None = None
