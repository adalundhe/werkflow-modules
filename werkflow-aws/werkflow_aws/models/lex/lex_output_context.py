from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexOutputContext(BaseModel):
    name: StrictStr | None = None
    timeToLiveInSeconds: StrictInt | None = None
    turnsToLive: StrictInt | None = None
