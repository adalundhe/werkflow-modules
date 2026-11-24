from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheDataStorage(BaseModel):
    Maximum: StrictInt | None = None
    Minimum: StrictInt | None = None
    Unit: StrictStr | None = None
