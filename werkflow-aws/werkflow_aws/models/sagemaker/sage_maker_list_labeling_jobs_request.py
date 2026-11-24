from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListLabelingJobsRequest(BaseModel):
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    LastModifiedTimeAfter: datetime.datetime | StrictStr | None = None
    LastModifiedTimeBefore: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    NameContains: StrictStr | None = None
    SortBy: Literal['Name', 'CreationTime', 'Status'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    StatusEquals: Literal['Initializing', 'InProgress', 'Completed', 'Failed', 'Stopping', 'Stopped'] | None = None
