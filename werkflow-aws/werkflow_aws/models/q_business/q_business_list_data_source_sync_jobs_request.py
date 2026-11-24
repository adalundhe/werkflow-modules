from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessListDataSourceSyncJobsRequest(BaseModel):
    dataSourceId: StrictStr
    applicationId: StrictStr
    indexId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    statusFilter: Literal['FAILED', 'SUCCEEDED', 'SYNCING', 'INCOMPLETE', 'STOPPING', 'ABORTED', 'SYNCING_INDEXING'] | None = None
