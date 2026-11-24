from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointQuietTime(BaseModel):
    End: StrictStr | None = None
    Start: StrictStr | None = None
