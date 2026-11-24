from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointClosedDaysRule(BaseModel):
    Name: StrictStr | None = None
    StartDateTime: StrictStr | None = None
    EndDateTime: StrictStr | None = None
