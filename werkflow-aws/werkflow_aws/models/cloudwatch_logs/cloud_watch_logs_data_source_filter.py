from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDataSourceFilter(BaseModel):
    name: StrictStr
    type: StrictStr | None = None
