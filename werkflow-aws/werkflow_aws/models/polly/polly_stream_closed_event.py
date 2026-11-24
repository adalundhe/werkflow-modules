from __future__ import annotations
from pydantic import BaseModel, StrictInt


class PollyStreamClosedEvent(BaseModel):
    RequestCharacters: StrictInt | None = None
