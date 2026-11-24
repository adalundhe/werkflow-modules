from __future__ import annotations
from pydantic import BaseModel, StrictInt


class WAFv2ImmunityTimeProperty(BaseModel):
    ImmunityTime: StrictInt | None = None
