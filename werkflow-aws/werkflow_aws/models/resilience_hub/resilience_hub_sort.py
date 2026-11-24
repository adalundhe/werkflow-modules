from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ResilienceHubSort(BaseModel):
    field: StrictStr
    ascending: StrictBool | None = None
