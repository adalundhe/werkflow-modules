from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListHubsRequest(BaseModel):
    NameContains: StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    LastModifiedTimeBefore: datetime.datetime | StrictStr | None = None
    LastModifiedTimeAfter: datetime.datetime | StrictStr | None = None
    SortBy: Literal['HubName', 'CreationTime', 'HubStatus', 'AccountIdOwner'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
