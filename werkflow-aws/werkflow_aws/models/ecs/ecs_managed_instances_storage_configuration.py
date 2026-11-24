from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ECSManagedInstancesStorageConfiguration(BaseModel):
    storageSizeGiB: StrictInt | None = None
