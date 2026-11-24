from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListAIRecommendationJobsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    NameContains: StrictStr | None = None
    StatusEquals: Literal['InProgress', 'Completed', 'Failed', 'Stopping', 'Stopped'] | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    SortBy: Literal['Name', 'CreationTime', 'Status'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
