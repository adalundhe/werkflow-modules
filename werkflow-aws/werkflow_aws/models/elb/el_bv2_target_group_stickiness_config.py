from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class ELBv2TargetGroupStickinessConfig(BaseModel):
    Enabled: StrictBool | None = None
    DurationSeconds: StrictInt | None = None
