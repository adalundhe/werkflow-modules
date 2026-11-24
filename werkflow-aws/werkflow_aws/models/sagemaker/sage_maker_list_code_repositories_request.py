from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListCodeRepositoriesRequest(BaseModel):
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    LastModifiedTimeAfter: datetime.datetime | StrictStr | None = None
    LastModifiedTimeBefore: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    NameContains: StrictStr | None = None
    NextToken: StrictStr | None = None
    SortBy: Literal['Name', 'CreationTime', 'LastModifiedTime'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
