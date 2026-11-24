from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeDocumentCharLocation(BaseModel):
    documentIndex: StrictInt | None = None
    start: StrictInt | None = None
    end: StrictInt | None = None
