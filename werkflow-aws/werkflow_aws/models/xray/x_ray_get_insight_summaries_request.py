from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class XRayGetInsightSummariesRequest(BaseModel):
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    States: list[Literal['ACTIVE', 'CLOSED']] | None = None
    GroupARN: StrictStr | None = None
    GroupName: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
