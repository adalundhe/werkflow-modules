from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheTag(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
