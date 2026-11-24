from __future__ import annotations
from pydantic import BaseModel, StrictBool


class AutoScalingInstanceMonitoring(BaseModel):
    Enabled: StrictBool | None = None
