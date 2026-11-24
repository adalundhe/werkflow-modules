from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BatchManagedInstancesStorageConfiguration(BaseModel):
    storageSizeGiB: StrictInt | None = None
