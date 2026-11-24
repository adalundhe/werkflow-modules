from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractExtractionGranularity(BaseModel):
    Types: list[StrictStr] | None = None
