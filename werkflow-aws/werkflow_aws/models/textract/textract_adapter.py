from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractAdapter(BaseModel):
    AdapterId: StrictStr
    Version: StrictStr
    Pages: list[StrictStr] | None = None
