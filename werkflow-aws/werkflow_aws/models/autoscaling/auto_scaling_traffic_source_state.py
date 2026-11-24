from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingTrafficSourceState(BaseModel):
    TrafficSource: StrictStr | None = None
    State: StrictStr | None = None
    Identifier: StrictStr | None = None
    Type: StrictStr | None = None
