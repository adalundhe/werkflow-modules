from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListClusterOperationsRequest(BaseModel):
    ClusterName: StrictStr
    Status: Literal['InProgress', 'Superseded', 'Done'] | None = None
    Type: Literal['Scaling', 'DeepHealthCheck'] | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    SortBy: Literal['CreationTime'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
