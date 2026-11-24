from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteKeys(BaseModel):
    withKeys: list[StrictStr] | None = None
