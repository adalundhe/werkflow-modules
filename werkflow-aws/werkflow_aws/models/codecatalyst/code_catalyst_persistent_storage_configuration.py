from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CodeCatalystPersistentStorageConfiguration(BaseModel):
    sizeInGiB: StrictInt
