from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListSubscriptionTargetsRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    sortBy: Literal['CREATED_AT', 'UPDATED_AT'] | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
