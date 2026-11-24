from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ResilienceHubListAppVersionsRequest(BaseModel):
    appArn: StrictStr
    endTime: datetime.datetime | StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
