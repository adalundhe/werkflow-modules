from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListDataSourceRunsRequest(BaseModel):
    domainIdentifier: StrictStr
    dataSourceIdentifier: StrictStr
    status: Literal['REQUESTED', 'RUNNING', 'FAILED', 'PARTIALLY_SUCCEEDED', 'SUCCESS'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
