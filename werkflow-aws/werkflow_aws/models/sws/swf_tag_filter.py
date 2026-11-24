from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFTagFilter(BaseModel):
    tag: StrictStr
