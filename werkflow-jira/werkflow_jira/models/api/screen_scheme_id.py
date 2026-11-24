from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ScreenSchemeId(BaseModel):
    id: StrictInt | None = None
