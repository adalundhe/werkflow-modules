from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TargetStatus(BaseModel):
    statuses: dict[StrictStr, list[StrictStr]] | None = None
