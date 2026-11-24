from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheGlobalNodeGroup(BaseModel):
    GlobalNodeGroupId: StrictStr | None = None
    Slots: StrictStr | None = None
