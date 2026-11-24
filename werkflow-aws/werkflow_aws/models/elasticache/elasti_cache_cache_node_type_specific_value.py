from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheCacheNodeTypeSpecificValue(BaseModel):
    CacheNodeType: StrictStr | None = None
    Value: StrictStr | None = None
