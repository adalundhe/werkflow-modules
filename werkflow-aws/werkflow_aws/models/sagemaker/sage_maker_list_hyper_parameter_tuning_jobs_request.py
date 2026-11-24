from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListHyperParameterTuningJobsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SortBy: Literal['Name', 'Status', 'CreationTime'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NameContains: StrictStr | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    LastModifiedTimeAfter: datetime.datetime | StrictStr | None = None
    LastModifiedTimeBefore: datetime.datetime | StrictStr | None = None
    StatusEquals: Literal['Completed', 'InProgress', 'Failed', 'Stopped', 'Stopping', 'Deleting', 'DeleteFailed'] | None = None
