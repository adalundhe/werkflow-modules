from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointHoldoutActivity(BaseModel):
    NextActivity: StrictStr | None = None
    Percentage: StrictInt | None = None
