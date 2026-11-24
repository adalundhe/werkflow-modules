from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerFSxLustreConfig(BaseModel):
    SizeInGiB: StrictInt | None = None
    PerUnitStorageThroughput: StrictInt | None = None
