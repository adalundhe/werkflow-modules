from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessGetIndexRequest(BaseModel):
    id: StrictStr
    indexName: StrictStr
