from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexListTestSetRecordsRequest(BaseModel):
    testSetId: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
