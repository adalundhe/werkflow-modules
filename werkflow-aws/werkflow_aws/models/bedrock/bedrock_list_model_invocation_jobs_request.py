from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListModelInvocationJobsRequest(BaseModel):
    submitTimeAfter: datetime.datetime | StrictStr | None = None
    submitTimeBefore: datetime.datetime | StrictStr | None = None
    statusEquals: Literal['Submitted', 'InProgress', 'Completed', 'Failed', 'Stopping', 'Stopped', 'PartiallyCompleted', 'Expired', 'Validating', 'Scheduled'] | None = None
    nameContains: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortBy: Literal['CreationTime'] | None = None
    sortOrder: Literal['Ascending', 'Descending'] | None = None
