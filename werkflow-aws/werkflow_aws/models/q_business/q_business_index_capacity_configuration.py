from __future__ import annotations
from pydantic import BaseModel, StrictInt


class QBusinessIndexCapacityConfiguration(BaseModel):
    units: StrictInt | None = None
