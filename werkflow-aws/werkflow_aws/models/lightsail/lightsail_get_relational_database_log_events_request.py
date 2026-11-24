from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailGetRelationalDatabaseLogEventsRequest(BaseModel):
    relationalDatabaseName: StrictStr
    logStreamName: StrictStr
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    startFromHead: StrictBool | None = None
    pageToken: StrictStr | None = None
