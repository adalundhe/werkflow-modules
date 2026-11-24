from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointWaitTime(BaseModel):
    WaitFor: StrictStr | None = None
    WaitUntil: StrictStr | None = None
