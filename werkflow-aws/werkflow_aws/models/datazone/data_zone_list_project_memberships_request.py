from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListProjectMembershipsRequest(BaseModel):
    domainIdentifier: StrictStr
    projectIdentifier: StrictStr
    sortBy: Literal['NAME'] | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
