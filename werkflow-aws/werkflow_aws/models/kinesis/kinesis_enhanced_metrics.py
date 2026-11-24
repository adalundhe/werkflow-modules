from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisEnhancedMetrics(BaseModel):
    ShardLevelMetrics: list[StrictStr] | None = None
