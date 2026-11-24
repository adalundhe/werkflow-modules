from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EMRPortRange(BaseModel):
    MinRange: StrictInt | None = None
    MaxRange: StrictInt | None = None
