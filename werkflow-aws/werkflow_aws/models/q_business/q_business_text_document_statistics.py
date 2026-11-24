from __future__ import annotations
from pydantic import BaseModel, StrictInt


class QBusinessTextDocumentStatistics(BaseModel):
    indexedTextBytes: StrictInt | None = None
    indexedTextDocumentCount: StrictInt | None = None
