from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CodeCatalystPersistentStorage(BaseModel):
    sizeInGiB: StrictInt | None = None
