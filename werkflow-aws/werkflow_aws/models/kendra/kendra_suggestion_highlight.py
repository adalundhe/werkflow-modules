from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KendraSuggestionHighlight(BaseModel):
    BeginOffset: StrictInt | None = None
    EndOffset: StrictInt | None = None
