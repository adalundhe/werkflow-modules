from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsUpperCaseString(BaseModel):
    withKeys: list[StrictStr] | None = None
