from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexPathFormat(BaseModel):
    objectPrefixes: list[StrictStr] | None = None
