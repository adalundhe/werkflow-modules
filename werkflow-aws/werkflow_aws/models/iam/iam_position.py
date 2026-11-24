from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IAMPosition(BaseModel):
    Line: StrictInt | None = None
    Column: StrictInt | None = None
