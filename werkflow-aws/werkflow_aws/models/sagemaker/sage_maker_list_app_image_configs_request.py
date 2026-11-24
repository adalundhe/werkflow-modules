from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListAppImageConfigsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    NameContains: StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    ModifiedTimeBefore: datetime.datetime | StrictStr | None = None
    ModifiedTimeAfter: datetime.datetime | StrictStr | None = None
    SortBy: Literal['CreationTime', 'LastModifiedTime', 'Name'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
