from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmListTestGridSessionsRequest(BaseModel):
    projectArn: StrictStr
    status: Literal['ACTIVE', 'CLOSED', 'ERRORED'] | None = None
    creationTimeAfter: datetime.datetime | StrictStr | None = None
    creationTimeBefore: datetime.datetime | StrictStr | None = None
    endTimeAfter: datetime.datetime | StrictStr | None = None
    endTimeBefore: datetime.datetime | StrictStr | None = None
    maxResult: StrictInt | None = None
    nextToken: StrictStr | None = None
