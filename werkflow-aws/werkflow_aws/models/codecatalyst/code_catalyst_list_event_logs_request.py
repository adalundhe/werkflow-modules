from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCatalystListEventLogsRequest(BaseModel):
    spaceName: StrictStr
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    eventName: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
