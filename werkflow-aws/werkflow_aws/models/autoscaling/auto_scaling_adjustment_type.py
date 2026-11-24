from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingAdjustmentType(BaseModel):
    AdjustmentType: StrictStr | None = None
