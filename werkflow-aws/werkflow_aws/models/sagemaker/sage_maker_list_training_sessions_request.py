from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListTrainingSessionsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    NameContains: StrictStr | None = None
    StatusEquals: Literal['Created', 'Blocked', 'Running', 'Failed', 'Scheduled', 'Stopping', 'Stopped', 'Expired', 'Deleting', 'DeletionFailed'] | None = None
