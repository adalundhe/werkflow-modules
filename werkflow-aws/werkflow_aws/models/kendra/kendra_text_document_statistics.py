from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KendraTextDocumentStatistics(BaseModel):
    IndexedTextDocumentsCount: StrictInt | None = None
    IndexedTextBytes: StrictInt | None = None
