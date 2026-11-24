from __future__ import annotations
from pydantic import BaseModel, StrictInt


class WorklogCompositeKey(BaseModel):
    issueId: StrictInt | None = None
    worklogId: StrictInt | None = None
