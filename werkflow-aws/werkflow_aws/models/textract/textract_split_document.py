from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TextractSplitDocument(BaseModel):
    Index: StrictInt | None = None
    Pages: list[StrictInt] | None = None
