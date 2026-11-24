from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListNotebooksRequest(BaseModel):
    domainIdentifier: StrictStr
    owningProjectIdentifier: StrictStr
    maxResults: StrictInt | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    sortBy: Literal['CREATED_AT', 'UPDATED_AT'] | None = None
    status: Literal['ACTIVE', 'ARCHIVED', 'SYNC_IN_PROGRESS', 'SYNC_FAILED'] | None = None
    type: Literal['DATA', 'SQL'] | None = None
    nextToken: StrictStr | None = None
