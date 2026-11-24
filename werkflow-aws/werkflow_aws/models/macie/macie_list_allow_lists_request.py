from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieListAllowListsRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
