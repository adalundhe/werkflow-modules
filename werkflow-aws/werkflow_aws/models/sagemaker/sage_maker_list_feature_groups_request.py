from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListFeatureGroupsRequest(BaseModel):
    NameContains: StrictStr | None = None
    FeatureGroupStatusEquals: Literal['Creating', 'Created', 'CreateFailed', 'Deleting', 'DeleteFailed'] | None = None
    OfflineStoreStatusEquals: Literal['Active', 'Blocked', 'Disabled'] | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    SortBy: Literal['Name', 'FeatureGroupStatus', 'OfflineStoreStatus', 'CreationTime'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
