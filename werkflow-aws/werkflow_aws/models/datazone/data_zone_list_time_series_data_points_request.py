from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListTimeSeriesDataPointsRequest(BaseModel):
    domainIdentifier: StrictStr
    entityIdentifier: StrictStr
    entityType: Literal['ASSET', 'LISTING']
    formName: StrictStr
    startedAt: datetime.datetime | StrictStr | None = None
    endedAt: datetime.datetime | StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
