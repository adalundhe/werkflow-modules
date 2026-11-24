from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDataSource(BaseModel):
    name: StrictStr | None = None
    type: StrictStr | None = None
