from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListNotificationsRequest(BaseModel):
    domainIdentifier: StrictStr
    type: Literal['TASK', 'EVENT']
    afterTimestamp: datetime.datetime | StrictStr | None = None
    beforeTimestamp: datetime.datetime | StrictStr | None = None
    subjects: list[StrictStr] | None = None
    taskStatus: Literal['ACTIVE', 'INACTIVE'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
