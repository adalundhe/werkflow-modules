from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListLineageEventsRequest(BaseModel):
    domainIdentifier: StrictStr
    maxResults: StrictInt | None = None
    timestampAfter: datetime.datetime | StrictStr | None = None
    timestampBefore: datetime.datetime | StrictStr | None = None
    processingStatus: Literal['REQUESTED', 'PROCESSING', 'SUCCESS', 'FAILED'] | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    nextToken: StrictStr | None = None
