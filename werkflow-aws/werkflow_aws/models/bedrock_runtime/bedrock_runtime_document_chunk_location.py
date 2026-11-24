from __future__ import annotations
from pydantic import BaseModel, StrictInt


class BedrockRuntimeDocumentChunkLocation(BaseModel):
    documentIndex: StrictInt | None = None
    start: StrictInt | None = None
    end: StrictInt | None = None
