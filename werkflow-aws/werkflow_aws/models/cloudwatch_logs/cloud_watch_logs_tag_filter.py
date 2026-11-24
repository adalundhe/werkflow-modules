from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsTagFilter(BaseModel):
    key: StrictStr
    values: list[StrictStr] | None = None
