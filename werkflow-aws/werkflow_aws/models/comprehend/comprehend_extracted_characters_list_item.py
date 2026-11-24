from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ComprehendExtractedCharactersListItem(BaseModel):
    Page: StrictInt | None = None
    Count: StrictInt | None = None
