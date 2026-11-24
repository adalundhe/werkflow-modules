from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsTrimString(BaseModel):
    withKeys: list[StrictStr] | None = None
