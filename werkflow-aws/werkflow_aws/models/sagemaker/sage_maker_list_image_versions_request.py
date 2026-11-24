from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListImageVersionsRequest(BaseModel):
    ImageName: StrictStr
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    LastModifiedTimeAfter: datetime.datetime | StrictStr | None = None
    LastModifiedTimeBefore: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    SortBy: Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'VERSION'] | None = None
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
