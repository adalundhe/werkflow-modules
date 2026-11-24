from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchServerlessListCollectionGroupsRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
