from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SageMakerListClusterNodesRequest(BaseModel):
    ClusterName: StrictStr
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    InstanceGroupNameContains: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    SortBy: Literal['CREATION_TIME', 'NAME'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    IncludeNodeLogicalIds: StrictBool | None = None
