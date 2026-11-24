from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EKSIntegerConstraints(BaseModel):
    min: StrictInt | None = None
    max: StrictInt | None = None
