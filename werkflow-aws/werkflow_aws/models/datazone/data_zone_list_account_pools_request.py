from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListAccountPoolsRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr | None = None
    sortBy: Literal['NAME'] | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
