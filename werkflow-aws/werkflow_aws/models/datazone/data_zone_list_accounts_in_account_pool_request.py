from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListAccountsInAccountPoolRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
