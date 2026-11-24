from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheEndpoint(BaseModel):
    Address: StrictStr | None = None
    Port: StrictInt | None = None
