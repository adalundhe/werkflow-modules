from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .kendra_time_range import KendraTimeRange


class KendraListDataSourceSyncJobsRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    StartTimeFilter: KendraTimeRange | None = None
    StatusFilter: Literal['FAILED', 'SUCCEEDED', 'SYNCING', 'INCOMPLETE', 'STOPPING', 'ABORTED', 'SYNCING_INDEXING'] | None = None
