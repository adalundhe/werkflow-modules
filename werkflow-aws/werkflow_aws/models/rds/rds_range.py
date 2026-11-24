from __future__ import annotations
from pydantic import BaseModel, StrictInt


class RDSRange(BaseModel):
    From: StrictInt | None = None
    To: StrictInt | None = None
    Step: StrictInt | None = None
