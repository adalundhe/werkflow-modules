from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FSxFileCacheLustreMetadataConfiguration(BaseModel):
    StorageCapacity: StrictInt | None = None
