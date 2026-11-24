from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFCancelTimerDecisionAttributes(BaseModel):
    timerId: StrictStr
