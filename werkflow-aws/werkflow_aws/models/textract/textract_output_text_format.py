from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractOutputTextFormat(BaseModel):
    Types: list[StrictStr] | None = None
