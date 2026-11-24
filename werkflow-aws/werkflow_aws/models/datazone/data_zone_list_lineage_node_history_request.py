from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListLineageNodeHistoryRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    direction: Literal['UPSTREAM', 'DOWNSTREAM'] | None = None
    eventTimestampGTE: datetime.datetime | StrictStr | None = None
    eventTimestampLTE: datetime.datetime | StrictStr | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
