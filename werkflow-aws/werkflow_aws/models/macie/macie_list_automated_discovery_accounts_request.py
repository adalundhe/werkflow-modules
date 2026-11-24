from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieListAutomatedDiscoveryAccountsRequest(BaseModel):
    accountIds: list[StrictStr] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
