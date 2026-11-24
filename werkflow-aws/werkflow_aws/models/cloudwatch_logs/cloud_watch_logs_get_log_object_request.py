from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsGetLogObjectRequest(BaseModel):
    logObjectPointer: StrictStr
    unmask: StrictBool | None = None
