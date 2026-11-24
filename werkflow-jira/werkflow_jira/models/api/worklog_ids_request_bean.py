from __future__ import annotations
from pydantic import BaseModel, StrictInt


class WorklogIdsRequestBean(BaseModel):
    ids: list[StrictInt] | None = None
