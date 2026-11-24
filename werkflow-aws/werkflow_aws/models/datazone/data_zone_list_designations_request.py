from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListDesignationsRequest(BaseModel):
    domainIdentifier: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
