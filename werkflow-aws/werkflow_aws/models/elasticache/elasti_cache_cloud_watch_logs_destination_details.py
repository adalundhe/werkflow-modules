from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheCloudWatchLogsDestinationDetails(BaseModel):
    LogGroup: StrictStr | None = None
