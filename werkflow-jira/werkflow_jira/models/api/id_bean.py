from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IdBean(BaseModel):
    id: StrictInt | None = None
