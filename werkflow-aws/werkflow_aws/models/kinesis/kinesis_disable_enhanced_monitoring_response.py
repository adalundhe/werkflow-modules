from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class KinesisDisableEnhancedMonitoringResponse(BaseModel):
    StreamName: StrictStr | None = None
    CurrentShardLevelMetrics: list[StrictStr] | None = None
    DesiredShardLevelMetrics: list[StrictStr] | None = None
    StreamARN: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
