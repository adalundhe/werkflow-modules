from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ECSEphemeralStorage(BaseModel):
    sizeInGiB: StrictInt | None = None
