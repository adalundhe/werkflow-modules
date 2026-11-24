from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveCreateGraphRequest(BaseModel):
    Tags: dict[StrictStr, StrictStr] | None = None
