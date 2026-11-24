from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_wait_time import PinpointWaitTime


class PinpointWaitActivity(BaseModel):
    NextActivity: StrictStr | None = None
    WaitTime: PinpointWaitTime | None = None
