from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCollectiveConstant(BaseModel):
    ValueList: list[StrictStr] | None = None
