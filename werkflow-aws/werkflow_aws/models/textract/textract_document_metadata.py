from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TextractDocumentMetadata(BaseModel):
    Pages: StrictInt | None = None
