from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsLowerCaseString(BaseModel):
    withKeys: list[StrictStr] | None = None
