from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeSearchResultLocation(BaseModel):
    searchResultIndex: StrictInt | None = None
    start: StrictInt | None = None
    end: StrictInt | None = None
