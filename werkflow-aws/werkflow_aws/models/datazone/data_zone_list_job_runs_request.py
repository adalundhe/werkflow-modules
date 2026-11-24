from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListJobRunsRequest(BaseModel):
    domainIdentifier: StrictStr
    jobIdentifier: StrictStr
    status: Literal['SCHEDULED', 'IN_PROGRESS', 'SUCCESS', 'PARTIALLY_SUCCEEDED', 'FAILED', 'ABORTED', 'TIMED_OUT', 'CANCELED'] | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
