from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ECSAcceleratorCountRequest(BaseModel):
    min: StrictInt | None = None
    max: StrictInt | None = None
