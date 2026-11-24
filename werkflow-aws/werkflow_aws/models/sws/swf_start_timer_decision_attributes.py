from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFStartTimerDecisionAttributes(BaseModel):
    timerId: StrictStr
    startToFireTimeout: StrictStr
    control: StrictStr | None = None
