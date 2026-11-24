from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsLogGroupField(BaseModel):
    name: StrictStr | None = None
    percent: StrictInt | None = None
