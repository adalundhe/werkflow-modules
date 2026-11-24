from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListLabelingJobsForWorkteamRequest(BaseModel):
    WorkteamArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    JobReferenceCodeContains: StrictStr | None = None
    SortBy: Literal['CreationTime'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
