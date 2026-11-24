from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECRListReplicationBackfillsRequest(BaseModel):
    registryId: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
