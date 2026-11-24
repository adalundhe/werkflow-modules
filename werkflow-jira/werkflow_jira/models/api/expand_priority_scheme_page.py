from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt


class ExpandPrioritySchemePage(BaseModel):
    model_config = ConfigDict(extra="allow")

    maxResults: StrictInt | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
