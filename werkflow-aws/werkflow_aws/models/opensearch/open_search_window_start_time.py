from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchWindowStartTime(BaseModel):
    Hours: StrictInt | None = None
    Minutes: StrictInt | None = None
