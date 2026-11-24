from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessListGroupsRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    updatedEarlierThan: datetime.datetime | StrictStr
    dataSourceId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
