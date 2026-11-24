from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchServerlessListIngestionJobsRequest(BaseModel):
    collectionId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
