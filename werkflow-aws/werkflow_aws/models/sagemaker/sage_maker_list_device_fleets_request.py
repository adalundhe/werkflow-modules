from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListDeviceFleetsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    LastModifiedTimeAfter: datetime.datetime | StrictStr | None = None
    LastModifiedTimeBefore: datetime.datetime | StrictStr | None = None
    NameContains: StrictStr | None = None
    SortBy: Literal['NAME', 'CREATION_TIME', 'LAST_MODIFIED_TIME'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
