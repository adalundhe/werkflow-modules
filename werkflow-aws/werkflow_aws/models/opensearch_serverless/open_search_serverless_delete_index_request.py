from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessDeleteIndexRequest(BaseModel):
    id: StrictStr
    indexName: StrictStr
