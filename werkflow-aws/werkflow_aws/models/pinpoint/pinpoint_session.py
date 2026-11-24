from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointSession(BaseModel):
    Id: StrictStr
    StartTimestamp: StrictStr
    Duration: StrictInt | None = None
    StopTimestamp: StrictStr | None = None
