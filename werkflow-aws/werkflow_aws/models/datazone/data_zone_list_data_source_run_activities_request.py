from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListDataSourceRunActivitiesRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    status: Literal['FAILED', 'PUBLISHING_FAILED', 'SUCCEEDED_CREATED', 'SUCCEEDED_UPDATED', 'SKIPPED_ALREADY_IMPORTED', 'SKIPPED_ARCHIVED', 'SKIPPED_NO_ACCESS', 'UNCHANGED'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
