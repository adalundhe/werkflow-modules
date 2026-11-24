from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BatchEphemeralStorage(BaseModel):
    sizeInGiB: StrictInt | None = None
