from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MacieRange(BaseModel):
    end: StrictInt | None = None
    start: StrictInt | None = None
    startColumn: StrictInt | None = None
